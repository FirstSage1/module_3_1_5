# Модуль 3_1 пространство имен.
# =========================================
calls = 0


def count_call():
    global calls
    calls += 1


def string_info(str_):  # Содание функции
    count_call()
    long_str_ = len(str_)
    hi_str_ = str_.upper()
    low_str_ = str_.lower()
    cort_str_ = long_str_, hi_str_, low_str_
    return cort_str_


result_1 = string_info("Рубеж")
print(result_1)
result_2 = string_info("Приход")
print(result_2)


def is_contains(string, list_to_search):
    count_call()
    for i in list_to_search:
        if string.upper() == i.upper():
            return True
    return False


result_1 = is_contains('Добр', ['добропорядочный', 'добр', 'добрый'])
print(result_1)
result_2 = is_contains('Добр', ['добропорядочный', 'Добро', 'добрый'])
print(result_2)
print(calls)
