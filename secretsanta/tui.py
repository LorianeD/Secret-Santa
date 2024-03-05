from typing import Dict, List


def _ask_for_int(prompt: str, max_value: int, min_value: int = 1) -> int:
    while True:
        try:
            user_number = int(input(prompt))
            if (min_value <= user_number <= max_value):
                print()
                return user_number
            print("La valeur saisie n'est pas correcte.")
        except ValueError:
            print("La valeur saisie n'est pas un nombre entier.")

        print("Entrer un nombre entre {} et {}".format(min_value, max_value))


def _print_home_menu() -> int:
    print("Que veux tu savoir ?")
    print("1. Je veux connaître tous les pères noël")
    print("2. De qui suis-je le père noël ?")
    print("3. Quitter")
    return _ask_for_int("", 3, 1)


def _print_all_pairings(pairing: Dict[str, str]) -> None:
    print("Voici la liste des pères noël :")
    for person_a, person_b in pairing.items():
        print(f"{person_a} => {person_b}")
    print()


def _get_receiver(giver: str, pairing: Dict[str, str]) -> str:
    if giver in pairing:
        return pairing[giver]
    else:
        return None


def _ask_user_name() -> str:
    return input("Quel est ton nom ? ")


def _check_if_person_exists(people: Dict[str, str], user_name: str) -> bool:
    return user_name in people


def _get_user_name(people: List[str]) -> str:
    user_name_is_correct = False
    user_name = ""
    while (not user_name_is_correct):
        user_name = _ask_user_name().capitalize()
        user_name_is_correct = _check_if_person_exists(people, user_name)
        if not user_name_is_correct:
            print(f"Tu n'es pas dans la liste, {people}.")

    print()
    return user_name


def _user_menu(people: List[str],
               pairing: Dict[str, str]) -> None:
    user_name = _get_user_name(people)
    receiver = _get_receiver(user_name, pairing)
    print(f"{user_name}, tu es le père noël de {receiver} !")
    print()


def _print_home_message() -> None:
    print("--------------------------")
    print("Bienvenue au Secret Santa !")
    print("--------------------------")
    print()


def home_menu(people: List[str], pairing: Dict[str, str]) -> None:
    """The main menu for the Secret Santa application.

    Args:
        people (List[str]): A list of the valid names.
        pairing (Dict[str, str]): A dictionary containing the Secret Santa pairings.

    """
    _print_home_message()
    while True:
        user_choice = _print_home_menu()
        if user_choice == 1:
            _print_all_pairings(pairing)
        elif user_choice == 2:
            _user_menu(people, pairing)
        elif user_choice == 3:
            exit_message()
            break
        else:
            print("Choix invalide")


def exit_message() -> None:
    """Exit message for the application."""
    print()
    print("--------------------------")
    print("Joyeux Noël !")
    print("--------------------------")
    print()
