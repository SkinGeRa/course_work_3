import pytest

from src.func import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data('../src/operations.json')
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 4
    assert len(get_filtered_data(test_data, filtered_by_from=True)) == 2


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert data[0]["date"] == "2023-07-03T18:35:29.512364"
    assert len(data) == 4


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['26.08.2019 Перевод организации \nMaestro 1596 83** **** 5199 --> Счет **9589\n31957.58 руб.\n', '03.07.2023 Перевод организации \n  --> Счет **5560\n8221.37 USD\n', '30.06.2018 Перевод организации \nСчет 7510 68** **** 6952 --> Счет **6702\n9824.07 USD\n', '23.03.2018 Открытие вклада \n  --> Счет **2431\n48223.05 руб.\n', '04.04.2019 Перевод со счета на счет \nСчет 1970 86** **** 8542 --> Счет **4188\n79114.93 USD\n']