import requests


def show_request():
    request = requests.Request(
        "GET",
        "https://www.instagram.com/zxqwetx"
    )
    prepared = request.prepare()

    print("Метод:", prepared.method)
    print("Адреса:", prepared.url)