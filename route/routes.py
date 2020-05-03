from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from data.sql_alchemy import db
from datetime import timedelta
from models.user import User

def init_routes(app):
    @app.route("/")
    def index():
        return render_template("home.html")

    @app.route("/management")
    def management():
        users = User.query.all()
        return render_template("management.html", users=users)

    @app.route("/user/<int:id>")
    @login_required
    def show_user(id):
        user = User.query.get(id)
        return render_template("user.html", user=user)

    @app.route("/user/delete/<int:id>")
    @login_required
    def user_delete(id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

        flash(message="Usuário deletado com sucesso!", category="success")
        return redirect("/management")

    @app.route("/register", methods=["GET","POST"])
    def register():
        if request.method == "POST":
            user = User()
            user.name = request.form["name"]
            user.email = request.form["email"]
            user.cpf = request.form["cpf"]
            user.password = generate_password_hash(request.form["password"])

            if user.email == "" or user.name == "" or user.cpf == "" or user.password == "":
                flash(message="Campos precisam ser preenchidos!", category="danger")
                return redirect(url_for("register"))

            db.session.add(user)
            db.session.commit()

            flash(message="Usuário registrado com sucesso!", category="success")
            return redirect(url_for("index"))

        return render_template("register.html")

    @app.route("/login", methods=["GET","POST"])
    def login():
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            remember = request.form["remember"]

            user = User.query.filter_by(email=email).first()

            if not user:
                flash(message="E-mail não cadastrado!", category="warning")
                return redirect(url_for("login"))

            if not check_password_hash(user.password, password):
                flash(message="E-mail ou Senha estão inválidos!", category="warning")
                return redirect(url_for("login"))
            
            login_user(user, remember=remember, duration=timedelta(days=1))
            return redirect(url_for("management"))

        return render_template("login.html")

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        flash(message="Volte sempre!", category="info")
        return redirect(url_for("index"))