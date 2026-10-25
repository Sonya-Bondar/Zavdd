import random

ORIGINS = ["Місяця", "Сонця", "Дракона", "Вовка", "Лісу", "Грому", "Туману",
           "Попелу", "Льоду", "Вогню", "Ворона", "Змії", "Болота", "Гір",
           "Моря", "Ночі", "Зорі", "Пустелі", "Вітру", "Грози"]

TYPES = ["Корінь", "Листок", "Гриб", "Квітка", "Ягода",
         "Кристал", "Луска", "Перо", "Насіння", "Мох"]

def create_ingredient_pool():
    pool = []
    try:
        for t in TYPES:
            for origin in ORIGINS:
                pool.append(t + " " + origin)
    except Exception as e:
        print("Помилка створення пулу інгредієнтів:", e)
    return pool

def random_ingredient(pool):
    try:
        return random.choice(pool)
    except Exception as e:
        print("Помилка вибору інгредієнта:", e)
    return None

def get_type(name):
    try:
        return name.split(" ")[0]
    except Exception as e:
        print("Помилка визначення типу:", e)
        return ""