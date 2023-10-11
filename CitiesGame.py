def load_cities():
    with open("cities.txt", "r", encoding="utf-8") as file:
        cities = file.read().splitlines()
    return cities


def get_last_letter(current_city):
    last_letter_current = current_city[-1]
    return last_letter_current


def is_valid_letter(first_letter_player, last_letter_current):
    if first_letter_player != last_letter_current:
        print(f"Название города должно начинаться с буквы '{last_letter_current.upper()}'. Попробуйте другой.")
        return False
    return True
