from datetime import datetime


def show_datetime():
    now = datetime.now()
    print("Поточна дата й час:", now.strftime("%d.%m.%Y %H:%M:%S"))