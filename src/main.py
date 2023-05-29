from func import get_data, get_filtered_data, get_last_values, get_formatted_data


def main():
    FILTERED_BY_FROM = True
    COUNT_LAST_VALUES = 5

    file_path = 'operations.json'
    data = get_data(file_path)

    data = get_filtered_data(data, filtered_by_from=FILTERED_BY_FROM)
    data = get_last_values(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)

    print("INFO: Вывод данных")
    for operation in data:
        print(operation)


if __name__ == '__main__':
    main()
