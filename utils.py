__name__ = "utils"

def read_guess():
    return input("Podaj swój strzał: ")


def read_data_base(file_name):
    with open(file_name) as f:
        date_base = f.readlines()
    return date_base
