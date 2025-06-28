import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'-?\d+(?:\.\d+)?'    # Шаблон для пошуку чисел
    for match in re.finditer(pattern, text):
        yield float(match.group())    # Перетворюємо на float і повертаємо через генератор

def sum_profit(text: str, func: Callable):
    return sum(func(text))    # Сума всіх чисел, які повертає генератор