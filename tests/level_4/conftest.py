import pytest
import os

from functions.level_4.two_students import Student

@pytest.fixture()
def create_student():
    def student(telegram_account: str = '@alexkorolev'):
        return Student(
            first_name='Alexander', 
            last_name='Korolev',
            telegram_account=telegram_account
        )
    return student

@pytest.fixture()
def create_students(create_student):
    def inner(count: int, **kwargs) -> list[Student]:
        return [create_student(**kwargs) for _ in range(count)]
    return inner

@pytest.fixture()
def filepath():
    path_to_file = 'test_file.txt'
    with open(path_to_file, 'w') as file_handler:
        file_handler.writelines(['1\n', ' #2\n', '3\n'])

    yield path_to_file
    os.remove(path_to_file)

@pytest.fixture()
def config_file_path():
    path_to_file = 'test_file.txt'
    with open(path_to_file, 'w') as file_handler:
        file_handler.writelines('''
[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[tool:app-config]
database_path: /path/to/database
max_connections: 10
log_level: DEBUG
extra_fields:
    age: int
    email: str
    salary: float

[topsecret.server.example]
Port = 50022
ForwardX11 = no
''')

    yield path_to_file
    os.remove(path_to_file)

@pytest.fixture()
def config_file_path_without_fields():
    path_to_file = 'test_file.txt'
    with open(path_to_file, 'w') as file_handler:
        file_handler.writelines('')

    yield path_to_file
    os.remove(path_to_file)