from ingradiens import TYPES

EFFECTS = ["здоров'я", "сили", "швидкості", "невидимості", "мудрості",
           "удачі", "вогнестійкості", "нічного бачення", "підводного дихання", "регенерації"]

SIZES = ["Мале зілля", "Зілля", "Велике зілля", "Еліксир", "Великий еліксир"]

def create_potion_pool():
    pool = []
    try:
        for size_index in range(len(SIZES)):
            for effect_index in range(len(EFFECTS)):
                potion = {"name": SIZES[size_index] + " " + EFFECTS[effect_index],
                          "recipe": [TYPES[effect_index], TYPES[(effect_index + size_index) % len(TYPES)]],
                          "price": 20 + size_index * 20 + effect_index * 2,
                          }
                pool.append(potion)
    except Exception as e:
        print("Помилка створення пулу зілль:", e)
    return pool