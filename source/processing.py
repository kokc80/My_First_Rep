from typing import Dict, List


def filter_by_state(banking_operations: List[Dict[str, str]], state: str = "EXECUTED") -> List:
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


# тестовый вывод
# print(sort_by_date(list_unsorted, reverse=True))
# print(filter_by_state(list_unsorted))
