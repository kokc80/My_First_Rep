from typing import Dict, List


def filter_by_state(banking_operations: List[Dict[str, str]], state: str = "EXECUTED") -> List:
    filtered_list: List = []
    for dict_item in banking_operations:
        if dict_item.get("state") == state:
            filtered_list.append(dict_item)
    return filtered_list


def sort_by_date(data_list: List, reverse1: bool = True) -> List:
    """Функия принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция
    должна возвращать новый список, отсортированный по дате (date)"""
    list_sorted: List = sorted(data_list, key=lambda x: x.get("date"), reverse=reverse1)
    return list_sorted
