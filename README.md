# Documentação do WebSite

## Para Executar localmente o WebSite

Primeiro passo: 
- criar um ambiente virtual no Linux

`pip install virtualenv`

`virtualenv .ambvir --python=python3.7`

`source .ambvir/bin/activate`


- criar um ambiente virtual no Windows

`pip install virtualenv`

`python -m venv .ambvir`

`.ambvir\Scripts\activate` ou `.ambvir\Scripts\activate.bat`


Segundo passo:
- Instale os pacotes com o comando `pip install -r requirements/base.txt`
- Execute o comando `python app.py` e a aplicação rodará na url `http://127.0.0.1:5000/`.

***Obs***: Assim que solicitar uma requisição, será feito um DB.

## Rotas

- Url Main Page:

Rota: `http://127.0.0.1:5000/`


- Criar um Usuário:

Rota: `http://127.0.0.1:5000/register`


- Efeturar Login do Usuário:

Rota: `http://127.0.0.1:5000/login`


- Url Home:

Rota: `http://127.0.0.1:5000/management`


- Url Mostrar Usuário:

Rota: `http://127.0.0.1:5000/user/<int:id>`


- Deletar um Usuário:

Rota: `http://127.0.0.1:5000/user/delete/<int:id>`


- Efetuar Logout do Usuário:

Rota: `http://127.0.0.1:5000/logout`


- Adicionar Livros no Banco de Dados:

Rota: `http://127.0.0.1:5000/book/add`


- Cadastrar Livros em Usuários:

Rota: `http://127.0.0.1:5000/user/<int:id>/add-book`


## Executando e testando o WebSite

***Obs***: Não é necessário o server está online.

- Para executar os testes:
Comando: `pytest -vv`

## Exemplo do Retorno de testes

(.ambvir) C:\Users\MyPc\Desktop\Estudo_Flask>pytest -vv
================================================= test session starts =================================================

platform win32 -- Python 3.7.4, pytest-5.4.1, py-1.8.1, pluggy-0.13.1 --
c:\users\MyPc\appdata\local\programs\python\python37-32\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\MyPc\Desktop\Estudo_Flask
collected 5 items

tests/test_app.py::test_home_if_return_200 PASSED                                                                [ 20%]

tests/test_app.py::test_if_have_registrar PASSED                                                                 [ 40%]

tests/test_app.py::test_if_have_logar PASSED                                                                     [ 60%]

tests/test_app.py::test_register_user PASSED                                                                     [ 80%]

tests/test_app.py::test_login_user PASSED                                                                        [100%]

================================================== 5 passed in 1.05s ==================================================
