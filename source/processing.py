from typing import List, Dict

def filter_by_state(banking_operations: List[Dict[str, str]], state: str = 'EXECUTED') -> List:
    """ Функция принимает на вход список словарей с данными о банковских операциях
    и параметр state, возвращает новый список, содержащий только те словари,
      у которых ключ state содержит переданное в функцию значение """
    filtered_list = []
    for dict_item in banking_operations:
        if dict_item.get('state') == state:
            filtered_list.append(dict_item)
    return filtered_list

def sort_by_date(data_list: list, data_key, descending=True) -> List:
    List_sorted = sorted(data_list, key=lambda x: x[data_key], reverse=descending)
    return(List_sorted)

List_unsorted=[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

#print(sort_by_date(List_unsorted, data_key = 'date', descending = True))

#print(filter_by_state(List_unsorted))

