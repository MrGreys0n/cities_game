import random


def load_cities():
    with open("cities.txt", "r", encoding="utf-8") as file:
        cities = file.read().splitlines()
    return cities


def computer_city(available_cities, used_cities, cities):
    computer_city = random.choice(available_cities)
    used_cities.append(computer_city.lower())
    print(f"Мой ход: {computer_city}")
    cities.remove(computer_city)
    return computer_city


def computer_move(cities, used_cities, current_city):
    last_letter_current = get_last_letter(current_city)
    available_cities = get_available_cities(last_letter_current, cities, used_cities)
    if available_cities:
        return computer_city(available_cities, used_cities, cities)
    else:
        print("Я не могу найти подходящий город. Вы выиграли!")
        return 0


def end_game(player_city):
    if player_city == "выход":
        print("Игра окончена. До свидания!")
        return True
    return False


def is_city_used(player_city, used_cities):
    if player_city in used_cities:
        print("Этот город уже был использован. Попробуйте другой.")
        return True
    return False


def is_city(player_city, cities_lower):
    if player_city not in cities_lower:
        print("Такого города не существует. Попробуйте другой.")
        return False
    return True


def get_available_cities(letter, cities, used_cities):
    return [city for city in cities if city.lower() not in used_cities and city[0].lower() == letter]


def no_cities_available(letter, cities, used_cities):
    return len(get_available_cities(letter, cities, used_cities)) == 0


def get_last_letter(current_city):
    last_letter_current = current_city[-1].lower()
    if last_letter_current == "ы" or last_letter_current == "ь":
        last_letter_current = current_city[-2].lower()
    return last_letter_current


def is_valid_letter(first_letter_player, last_letter_current):
    if first_letter_player != last_letter_current:
        print(f"Название города должно начинаться с буквы '{last_letter_current.upper()}'. Попробуйте другой.")
        return False
    return True


def city_game():
    print('Добро пожаловать в игру "Города"!')
    cities = load_cities()
    cities_lower = [word.lower() for word in cities]
    used_cities = []

    current_city = random.choice(cities)
    print(f"Я начну с города {current_city}")
    used_cities.append(current_city.lower())

    while True:
        if no_cities_available(current_city[-1], cities, used_cities):
            print(f"Городов на букву {current_city[-1]} больше нет! Ты проиграл!")
            break

        input_city = input("Ваш ход: ").strip().lower()

        if not input_city:
            continue

        player_city = input_city.lower()

        if end_game(player_city):
            break

        if is_city_used(player_city, used_cities):
            continue

        if not (is_city(player_city, cities_lower)):
            continue

        first_letter_player = player_city[0].lower()
        last_letter_current = get_last_letter(current_city)

        if not (is_valid_letter(first_letter_player, last_letter_current)):
            continue

        used_cities.append(player_city.lower())
        current_city = player_city
        current_city = computer_move(cities, used_cities, current_city)
        if current_city == 0:
            break

        if not cities:
            print("Поздравляем, Вы выиграли! Больше не осталось городов.")
            break



if __name__ == "__main__":
    city_game()
