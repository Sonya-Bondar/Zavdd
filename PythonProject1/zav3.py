products = {
    1: {"name": "Корм для котів", "price": 360.00, "stock": 20},
    2: {"name": "Корм для папуг", "price": 300.50, "stock": 15},
    3: {"name": "Корм для собак", "price": 370.99, "stock": 28},
    4: {"name": "іграшка для тваринок (мала)", "price": 80.00, "stock": 40},
    5: {"name": "іграшка для тваринок (велика)", "price": 400.00, "stock": 40},
    6: {"name": "наповнювач 5л", "price": 380.00, "stock": 34},
}

cart=[]

def show_message(message, *args, **kwargs):
    print(message, *args, **kwargs)

def catalog():
    print("\n--- КАТАЛОГ ---")
    for product_id, product in products.items():
        print(
            f"{product_id}. {product["name"]} -"
            f"{product["price"]:.2f} грн"
            f"(залишок: {product["stock"]})"
        )
def add_to_cart(product_id):
    if product_id in products and products[product_id]["stock"]>0:
        cart.append(product_id)
        products[product_id]["stock"]-=1
        print("товар додано до кошика!")
    else:
        print("товар недоступний!")
def show_cart():
    if not cart:
        print("\nКошик порожній")
        return
    print("\n---КОШИК---")
    for product_id in cart:
        product=products[product_id]
        print(f"{product["name"]} - {product["price"]:.2f} грн")
    total= sum(
        map(lambda product_id: products[product_id]["price"], cart)
    )
    print(f"До сплати: {total:.2f} грн")
def remove_from_cart(product_id):
    if product_id in cart:
        cart.remove(product_id)
        products[product_id]["stock"] +=1
        print("Товар видалено з кошику")
    else:
        print("Такого товару немає в кошику")
def buy():
    if not cart:
        print("Кошик порожній")
        return
    total= sum(
        map(lambda product_id: products[product_id]["price", cart])
    )
    print(f"До сплати: {total:.2f} грн")
    answer=input("Підтвердити покупку? (так/ні):")
    if answer.lower()== "так":
        cart.clear()
        print("Покупку здійснено!")
    else:
        print("Покупку скасовано.")
def admin(login, password, **kwargs):
    if login== "admin" and password== "21112009":
        print("\n---ЗАЛИШКІ ТОВАРІВ---")
        for product in products.values():
            print(
                f"{product["name"]}: "
                f"{product["stock"]} шт."
            )
               
        if kwargs:
                print("Додатково інформація:", kwargs)
    else:
         print("Неправильний логін або пароль.")
def main():
    while True:
        print("\n--МІНІ-МАГАЗИН--")
        print("1- Каталог")
        print("2- Додати товар")
        print("3- Переглянути кошик")
        print("4- Видалити товар")
        print("5-Купити")
        print("6-Адміністратор")
        print("0-Вийти")
        choice=input("Ваш вибір:")

        if choice=="1":
            catalog()
        elif choice =="2":
            catalog()
            try:
                add_to_cart(int(input("Номер товару")))
            except ValueError:
                print("Введіть число:")
        elif choice=="3":
            show_cart()
        elif choice == "4":
            try:
                add_to_cart(int(input("Номер товару")))
            except ValueError:
                print("Введіть число:")
        elif choice=="5":
            buy()
        elif choice=="6":
            login =input("Логін:")
            password =input("Пароль:")
            admin(login, password, role="administrator")
        elif choice=="0":
            print("Дякуємо за покупку!")
            break
        else:
            print("Невірний вибір.")
if __name__=="__main__":
    main()








