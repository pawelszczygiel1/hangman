__name__ = "utils"


def read_guess():
    return input("Enter your try: ")


def read_data_base(file_name):
    with open(file_name) as f:
        date_base = f.readlines()
    return date_base
