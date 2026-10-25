from ingradiens import create_ingredient_pool
from potions import create_potion_pool
from game import game_loop

def main():
    try:
        ingredient_pool = create_ingredient_pool()
        potion_pool = create_potion_pool()
        print("Ти алхімік. Назбирай золото, варячи й продаючи зілля!")
        game_loop(ingredient_pool, potion_pool)
    except KeyboardInterrupt:
        print("\nГру припинено.")
    except Exception as e:
        print("Критична помилка!:", e)

if __name__ == "__main__":
    main()  