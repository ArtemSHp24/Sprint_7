import random
import string


def random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_courier():
    return {
        "login": random_string(),
        "password": random_string(),
        "firstName": random_string()
    }
