from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Length, Email, DataRequired, Regexp
from models.book import Book

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O Campo deve conter entre '3' á '6' caracteres.")
    ])
    remember = BooleanField("Permanecer Conectado")
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        Length(5, 25, "O Campo deve conter entre '5' á '25' caracteres."),
        DataRequired("Campo Requerido!")
    ])
    cpf = StringField("CPF", validators=[
        Regexp(regex=r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$', message="Digite um CPF válido."),
        DataRequired("Campo Requerido!")
    ])
    email = EmailField("Email", validators=[
        Email('Digite um e-mail válido.'),
        DataRequired("Campo Requerido!")
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O Campo deve conter entre '3' á '6' caracteres."),
        DataRequired("Campo Requerido!")
    ])
    submit = SubmitField("Registrar")

class BookForm(FlaskForm):
    name = StringField("Nome do livro", validators=[
        Length(1, 125, "O Campo não deve conter mais que '125' caracteres."),
        DataRequired("Campo Requerido!")
    ])
    submit = SubmitField("Adicionar")


class UserBookForm(FlaskForm):
    book = SelectField("Selecione um livro", coerce=int)
    submit = SubmitField("Adicionar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book.choices = [
           (book.id, book.name) for book in Book.query.all()
        ]