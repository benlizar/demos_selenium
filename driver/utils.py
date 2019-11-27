from faker import Faker


def get_random_name():
    fake = Faker()
    return fake.name()


def get_random_address():
    fake = Faker()
    return fake.address()


def get_random_phone_number():
    fake = Faker()
    return fake.msisdn()
