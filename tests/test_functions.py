import pytest
from utils import functions


def test_get_last_transactions():
    """
    Тестирование функции, которая возвращает список из 5 последних выполненных операций, начиная с последней операции
    """
    assert functions.get_last_transactions() == [
        {'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309',
         'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод с карты на счет', 'from': 'Maestro 1308795367077170',
         'to': 'Счет 96527012349577388612'},
        {'id': 957763565, 'state': 'EXECUTED', 'date': '2019-01-05T00:52:30.108534',
         'operationAmount': {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 46363668439560358409',
         'to': 'Счет 18889008294666828266'},
        {'id': 207126257, 'state': 'EXECUTED', 'date': '2019-07-15T11:47:40.496961',
         'operationAmount': {'amount': '92688.46', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Открытие вклада', 'to': 'Счет 35737585785074382265'},
        {'id': 921286598, 'state': 'EXECUTED', 'date': '2018-03-09T23:57:37.537412',
         'operationAmount': {'amount': '25780.71', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Счет 26406253703545413262', 'to': 'Счет 20735820461482021315'},
        {'id': 179194306, 'state': 'EXECUTED', 'date': '2019-05-19T12:51:49.023880',
         'operationAmount': {'amount': '6381.58', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'МИР 5211277418228469', 'to': 'Счет 58518872592028002662'}]


def test_transaction_in_class():
    """
    Тестирование функции, которая делает из элементов прошлого списка экземпляры классов
    """
    assert str(type(functions.transaction_in_class()[0])) == "<class 'utils.classes.Transaction'>"
    assert str(type(functions.transaction_in_class()[1])) == "<class 'utils.classes.Transaction'>"
    assert str(type(functions.transaction_in_class()[2])) == "<class 'utils.classes.Transaction'>"
    assert str(type(functions.transaction_in_class()[3])) == "<class 'utils.classes.Transaction'>"
    assert str(type(functions.transaction_in_class()[4])) == "<class 'utils.classes.Transaction'>"
