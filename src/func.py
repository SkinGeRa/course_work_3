import json
from datetime import datetime


def get_data(filepath):
    """
    :return Список операций в data
    """
    # with open("operations.json", "r", encoding="utf-8") as file:
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_filtered_data(data, filtered_by_from=False):
    """
    Фильтрует данные об операциях.
    Оставляет в data проведенные операции (executed) и операции имеющие поле "from"
    :param data: Список операций
    :param filtered_by_from: если передается True - происходит фильтрация по полю "from"
    :return: Список операций в data
    """
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filtered_by_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_values(data, count_last_values):
    """
    Сортирует список операций по дате и возвращает последние n операций
    :param data: Список операций
    :param count_last_values: количество операций которые нужно вернуть
    :return: data с n операций
    """
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    """
    Изменяет формат вывода информации об операции.
    :param data: Список операций
    :return: formatted_data: Информация об операции в измененном формате
    """
    formatted_data = []
    for i in data:
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = i["description"]
        from_info, from_bill = "", ""

        if "from" in i:
            sender = i["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f'{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}'
            from_info = " ".join(sender)

        to = f"{i['to'].split()[0]} **{i['to'][-4:]}"
        operation_amount = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
        formatted_data.append(f'{date} {description} \n'
                              f'{from_info} {from_bill} --> {to}\n'
                              f'{operation_amount}\n')

    return formatted_data
