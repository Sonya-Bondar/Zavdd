from tabulate import tabulate


def show_table():
    data = [
        ["Python", "Мова програмування"],
        ["PyCharm", "Редактор коду"],
        ["GitHub", "Платформа для проєктів"]
    ]
    print(tabulate(data, headers=["Назва", "Опис"], tablefmt="grid"))