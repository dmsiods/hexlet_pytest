from datetime import datetime
from pytest import fixture


# одна текущая дата на все тесты
now = datetime.now()


def test_foo():
    print(now)


def test_bar():
    print(now)


@fixture
def current_date():
    return datetime.now()


def test_datetime1(current_date):
    print(current_date)


def test_datetime2(current_date):
    print(current_date)


# Создаем фикстуру
# Запускается перед каждым тестом
@fixture
def coll(): # имя фикстуры выбирается произвольно
    return ['One', True, 3, [1, 'hexlet', [0]], 'cat', {}, '', [], False]

# Pytest сам прокидывает результат вызова функции там, где функция указана в аргументе
# Имя параметра совпадает с именем фикстуры
def test_compact(coll):
    result = bool(coll)
    assert result
