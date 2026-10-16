from faker import Faker


def show_fake_data():
    fake = Faker("uk_UA")
    print("Ім'я:", fake.name())
    print("Місто:", fake.city())
    print("Email:", fake.email())