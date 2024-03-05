from typing import List, Tuple, Dict
import itertools
import math
import random


class SecretSanta:
    def __init__(self, people: List[str], couples: List[Tuple[str, str]]) -> None:
        """
        Initialize a SecretSanta object.

        Args:
            people (List[str]): A list of person's names.
            couples (List[Tuple[str, str]]): A list of couples, where each tuple 
                represents a couple.
        """
        self.people_ = people
        self.couples_ = couples
        random.shuffle(self.people_)
        random.shuffle(self.couples_)
        self.gifts_ = {}

        if (not self._is_possible()):
            raise Exception("Couples or people list is not valid.")

        self.givers_ = people.copy()
        self.receivers_ = people.copy()

        self._create_groups()

    def _is_possible(self) -> bool:
        return (0 == len(self.couples_) and 3 <= len(self.people_)
                or 4 <= len(self.people_))

# Init functions
    def _get_nb_groups(self) -> int:
        nb_people: int = len(self.people_)
        nb_couples: int = len(self.couples_)

        nb_lovers = nb_couples*2
        if (nb_couples % 2 == 0
                or nb_people >= nb_lovers + 2):
            return 2
        else:
            return 3

    def _create_groups(self) -> None:
        """
        Create groups without separating couples

        This function creates a list of groups, where each group is a set of people.
        It does not separate couples, but instead distributes them evenly among the groups.
        The function takes into account the number of couples and the number of people,
        and ensures that each group has the correct number of people.
        """
        nb_groups: int = self._get_nb_groups()
        self.groups_ = [set() for _ in range(nb_groups)]

        # Dispatch couples in each groups
        for couple_index in range(len(self.couples_)):
            group_index = couple_index % nb_groups
            self.groups_[group_index].update(self.couples_[couple_index])

        people_in_couple = itertools.chain(*self.couples_)
        remaining_people = list(set(self.people_) - set(people_in_couple))
        nb_people_by_group: int = math.floor(len(self.people_) / nb_groups)

        # Dispatch remaining persons in each groups
        for group in self.groups_:
            nb_person_needed = nb_people_by_group - len(group)
            persons_for_this_group = remaining_people[:nb_person_needed]
            group.update(persons_for_this_group)
            remaining_people = remaining_people[nb_person_needed:]

        self.remaining_person_ = remaining_people[0] if remaining_people else None

# Gift distribution
    def _give_present(self, giver: str, receiver: str) -> None:
        self.gifts_[giver] = receiver
        self.givers_.remove(giver)
        self.receivers_.remove(receiver)

    def _get_available_receivers(self, giver: str, group_index: int) -> List[str]:
        # Get people in a specific group who have not yet received gift
        potential_receiver = list(set(self.groups_[group_index])
                                  & set(self.receivers_))

        # Check mutual gift
        for receiver in potential_receiver:
            if giver == self.gifts_.get(receiver):
                potential_receiver.remove(receiver)
                break

        return potential_receiver

    def compute_distribution(self) -> Dict[str, str]:
        """
        Computes the Secret Santa gift distribution.

        This function computes the Secret Santa gift distribution by assigning 
        a receipient of each person.
        It separate people in several groups. 
        Each group will offer its gifts to another group. By adding persons in 
        couple in a same group, this prevents peoples from a couple to receive 
        a gift from their lover.

        Returns:
            Dict[str, str]: A dictionary that maps each person to their gift 
            recipient.
        """

        nb_groups = len(self.groups_)

        # Reserve the first "giver" as the last "receiver"
        first_giver = list(self.groups_[0])[0]
        self.receivers_.remove(first_giver)

        giver = first_giver
        if self.remaining_person_:
            self._give_present(giver, self.remaining_person_)
            giver = self.remaining_person_

        receiver_group_index = 1
        while (self.receivers_):
            potential_receivers = self._get_available_receivers(
                giver,
                receiver_group_index
            )
            receiver = random.choice(potential_receivers)
            self._give_present(giver, receiver)

            giver = receiver
            receiver_group_index = (receiver_group_index+1) % nb_groups

        # Last "receiver" will give to the first "giver"
        self.gifts_[giver] = first_giver
        self.givers_.remove(giver)

        return self.gifts_
