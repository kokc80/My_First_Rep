from typing import Dict, List


def filter_by_state(
    banking_operations: List[Dict[str, str]], state: str = "EXECUTED"
) -> List:
    """Функция принимает на вход список словарей с данными о банковских
    операциях и параметр state, возвращает новый список, содержащий только
    те словари, у которых ключ state содержит переданное в функцию значение"""
    filtered_list: List = []
    for dict_item in banking_operations:
        if dict_item.get("state") == state:
            filtered_list.append(dict_item)
    return filtered_list


def sort_by_date(data_list: list, reverse: bool = True) -> List:
    """Функия принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция
    должна возвращать новый список, отсортированный по дате (date)
    )"""
    list_sorted: List = sorted(data_list, key=lambda x: x.get("date"), reverse=True)
    return list_sorted


list_unsorted: List = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# тестовый вывод
# print(sort_by_date(list_unsorted, reverse=True))
# print(filter_by_state(list_unsorted))
