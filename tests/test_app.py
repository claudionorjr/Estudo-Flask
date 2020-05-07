import pytest
from src import create_app
from src.sql_alchemy import db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "123456"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
    app.config["WTF_CSRF_ANABLED"] = False

    context = app.app_context()
    context.push()
    db.create_all()

    yield app.test_client()

    db.session.remove()
    db.drop_all()
    context.pop()

daties_register = { "name": "Testando", "cpf": "02345678955", "email": "joao@gmail.com", "password": "123546"}
daties_login = { "email": "joao@gmail.com", "password": "123546"}

def test_home_if_return_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_if_have_registrar(client):
    response = client.get("/")
    assert "Registrar" in response.get_data(as_text=True)

def test_if_have_logar(client):
    response = client.get("/")
    assert "Logar" in response.get_data(as_text=True)

def test_register_user(client):
    response = client.post("/register", data=daties_register, follow_redirects=True)
    assert "Testando" in response.get_data(as_text=True)

def test_login_user(client):
    response_to_register = client.post("/register", data=daties_register, follow_redirects=True)
    response = client.post("/login", data=daties_login, follow_redirects=True)
    assert response.status_code == 200