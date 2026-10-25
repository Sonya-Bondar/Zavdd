import config
from ingradiens import random_ingredient
from inventory import (add_item, remove_item, count_type, remove_by_type,
                       can_add, count_item, print_inventory)

def new_game(ingredient_pool):
    state = {"gold": config.START_GOLD, "day": 1, "ingredients": [], "potions": []}
    try:
        give_daily_ingredients(state, ingredient_pool)
    except Exception as e:
        print("Помилка створення гри:", e)
    return state

def give_daily_ingredients(state, ingredient_pool):
    try:
        print("Ти знайшов нові інгредієнти:")
        for _ in range(config.DAILY_INGREDIENTS):
            name = random_ingredient(ingredient_pool)
            left = add_item(state["ingredients"], name, 1,
                            config.INGREDIENT_SLOTS, config.INGREDIENT_STACK)
            if left == 0:
                print("  + " + name)
            else:
                print("  (немає місця, " + name + " викинуто)")
    except Exception as e:  # якщо сталась помилка
        print("Помилка видачі інгредієнтів:", e)

def show_status(state):
    try:
        print("\n=== День " + str(state["day"]) + "/" + str(config.MAX_DAYS) +
              " | Золото: " + str(state["gold"]) + "/" + str(config.GOAL_GOLD) + " ===")
        print_inventory(state["ingredients"], "Інгредієнти", config.INGREDIENT_SLOTS)
        print_inventory(state["potions"], "Зілля", config.POTION_SLOTS)
    except Exception as e:
        print("Помилка показу статусу:", e)

def show_recipes(potion_pool):
    try:
        print("--- Рецепти (потрібні типи інгредієнтів) ---")
        for i in range(len(potion_pool)):
            p = potion_pool[i]
            print(str(i + 1) + ". " + p["name"] + " | " + p["recipe"][0] + " + " +
                  p["recipe"][1] + " | ціна: " + str(p["price"]))
    except Exception as e:
        print("Помилка показу рецептів:", e)

def craft_potion( state, potion_pool):
    try:
        show_recipes(potion_pool)
        choice = int(input("Номер зілля (0 - назад): "))
        if choice == 0:
            return
        if choice < 1 or choice > len(potion_pool):
            print("Немає такого зілля!")
            return
        potion = potion_pool[choice - 1]

        need = {}
        for t in potion["recipe"]:
            if t in need :
                need[t] += 1
            else:
                need[t] = 1

        for t in need:
            if count_type(state["ingredients"], t) < need[t]:
                print("Не вистачає: " + t + " (треба " + str(need[t]) + ")")
                return

        if not can_add(state["potions"], potion["name"], config.POTION_SLOTS, config.POTION_STACK):
            print("Інвентар із зіллями повний! Продай зілля.")
            return

        for t in potion["recipe"]:
            remove_by_type(state["ingredients"], t)
        add_item(state["potions"], potion["name"], 1, config.POTION_SLOTS, config.POTION_STACK)
        print("Ви зварили: " + potion["name"] + "!")
    except ValueError:
        print("Треба ввести число!")
    except Exception as e:
        print("Помилка варіння:", e)

def sell_potions(state, potion_pool):
    try:
        prices = {}
        for p in potion_pool:
            prices[p["name"]] = p["price"]

        earned = 0
        while len(state["potions"]) > 0:
            slot = state["potions"].pop(0)
            earned += prices[slot["name"]] * slot["count"]
        state["gold"] += earned
        print("Продано зілля на " + str(earned) + " золота.")
    except Exception as e:
        print("Помилка продажу:", e)

def check_ending(state):
    try:
        if state["gold"] >= config.GOAL_GOLD:
            return "win"
        if state["day"] > config.MAX_DAYS:
            return "lose"
        return None
    except Exception as e:
        print("Помилка перевірки кінця:", e)
        return None

def end_day(state, potion_pool, ingredient_pool):
    try:
        print("\n--- Кінець дня " + str(state["day"]) + " ---")
        answer = input("Продати всі зілля? (yes/no): ").lower()
        if answer == "yes":
            sell_potions(state, potion_pool)
        elif answer == "no":
            print("Зілля залишаються в інвентарі.")
        else:
            print("Не зрозуміло, зілля не продаю.")

        if check_ending(state) == "win":
            return "win"

        if state["gold"] < config.RENT:
            print("Не вистачило золота на оренду лабораторії...")
            return "lose"
        state["gold"] -= config.RENT
        print("Сплачено оренду: " + str(config.RENT) + " золота.")

        state["day"] += 1
        if check_ending(state) == "lose":
            return "lose"

        give_daily_ingredients(state, ingredient_pool)
        return None
    except Exception as e:
        print("Помилка завершення дня:", e)
        return None  # гра

def show_ending(result, state):
    try:
        if result == "win":
            print("\n*** ПЕРЕМОГА! ")
            print("Ви назбирали " + str(state["gold"]) + " золота за " + str(state["day"]) +
                  " днів і купили найкращу лабораторію в місті. Ви стали Великим Алхіміком!")
        elif result == "lose":
            print("\n ПОРАЗКА ***")
            print("Золота не вистачило: " + str(state["gold"]) + "/" + str(config.GOAL_GOLD) +
                  ". Лабораторію забрали за борги, а ви пішли збирати трави в лісі...")
    except Exception as e:
        print("Помилка показу кінцівки:", e)

def game_loop(ingredient_pool, potion_pool):
    state = new_game(ingredient_pool)
    result = None
    while result is None:
        try:
            show_status(state)
            print("\n1 - Рецепти | 2 - Зварити зілля | 3 - Закінчити день | 0 - Вийти")
            choice = input("> ")
            if choice == "1":
                show_recipes(potion_pool)
            elif choice == "2":
                craft_potion(state, potion_pool)
            elif choice == "3":
                result = end_day(state, potion_pool, ingredient_pool)
            elif choice == "0":
                print("Вихід з гри.")
                return
            else:
                print("Невірна команда!")
        except Exception as e:
            print("Помилка в головному циклі:", e)
    show_ending(result, state)