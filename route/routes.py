from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from src.sql_alchemy import db
from datetime import timedelta
from models.user import User
from models.book import Book
from src.templates.forms import LoginForm, RegisterForm, BookForm, UserBookForm

def init_routes(app):
    @app.route("/")
    def index():
        return render_template("home.html")

    @app.route("/management")
    @login_required
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
        form = RegisterForm()

        if form.validate_on_submit():
            if User.query.filter_by(email=form.email.data).first():
                flash(message="Email já cadastrado!", category="warning")
                return redirect(url_for("register"))

            user = User()
            user.name = form.name.data
            user.email = form.email.data
            user.cpf = form.cpf.data
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()
            flash(message="Usuário registrado com sucesso!", category="success")
            return redirect(url_for("index"))

        return render_template("register.html", form=form)

    @app.route("/login", methods=["GET","POST"])
    def login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()

            if not user:
                flash(message="E-mail não cadastrado!", category="warning")
                return redirect(url_for("login"))

            if not check_password_hash(user.password, form.password.data):
                flash(message="E-mail ou Senha estão inválidos!", category="warning")
                return redirect(url_for("login"))
            
            login_user(user, remember=form.remember.data, duration=timedelta(days=1))
            return redirect(url_for("management"))

        return render_template("login.html", form=form)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        flash(message="Volte sempre!", category="info")
        return redirect(url_for("index"))

    @app.route("/book/add", methods=["GET","POST"])
    @login_required
    def add_book():
        form = BookForm()

        if form.validate_on_submit():
            book = Book()
            book.name = form.name.data

            db.session.add(book)
            db.session.commit()
            flash(message="Livro Adicionado com sucesso!", category="success")
            return redirect(url_for("add_book"))

        return render_template("add_book.html", form=form)

    @app.route("/user/<int:id>/add-book", methods=["GET","POST"])
    @login_required
    def user_add_book(id):
        form = UserBookForm()

        if form.validate_on_submit():
            book = Book.query.get(form.book.data)
            current_user.books.append(book)

            db.session.add(current_user)
            db.session.commit()

            flash(message="Livro Adicionado com sucesso!", category="success")
            return redirect(url_for("user_add_book", id=current_user.id))

        return render_template("user_add_book.html", form=form)