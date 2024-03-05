from typing import List, Tuple, Dict


def _are_lovers(supposed_couple: Tuple[str, str], couples: List[Tuple[str, str]]) -> bool:
    (person_a, person_b) = supposed_couple
    return (person_a, person_b) in couples or (person_b, person_a) in couples


def is_gifts_valid(people: List[str], couples: List[Tuple[str, str]], gifts: Dict[str, str]) -> bool:
    if len(people) != len(gifts):
        print("Tout le monde n'a pas offert 1 cadeau.")
        return False

    receivers = set(gifts.values())
    if len(people) != len(receivers):
        print("Tout le monde n'a pas reçu 1 cadeau.")
        return False

    for giver, receiver in gifts.items():
        if giver == receiver:
            print("Une personne s'offre lui même un cadeau.")
            return False
        elif giver == gifts[receiver]:
            print("2 personnes s'échangent des cadeaux entre eux.")
            return False
        elif _are_lovers((giver, receiver), couples):
            print("Au moins une personne offre un cadeau à sa moitié.")
            return False

    return True
