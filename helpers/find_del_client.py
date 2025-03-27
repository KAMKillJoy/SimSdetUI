"""
Модуль с методом поиска клиента, который подходит под критерии удаления:
- Длина имени ближе всего к среднеарифметической длине всех имён
"""

def find_del_client(client_names_list):
    name_len_sum = 0
    del_client = ""
    for name in client_names_list:
        name_len_sum += len(name)
    av_name_len = name_len_sum / len(client_names_list)
    closest = 999
    for name in client_names_list:
        avdif = abs(len(name) - av_name_len)
        if avdif < closest:
            del_client = name
            closest = avdif

    return del_client