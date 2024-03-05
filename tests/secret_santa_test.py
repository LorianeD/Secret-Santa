import unittest
from secretsanta.secret_santa import SecretSanta


class SecretSantaTest(unittest.TestCase):
    def test_get_nb_groups(self):
        people = ["Florent", "Jessica", "Ambroise",
                  "Bastien", "Coline", "Emilien"]
        couples = [("Florent", "Jessica"),
                   ("Coline", "Emilien"),
                   ("Ambroise", "Bastien")]
        secret_santa = SecretSanta(people, couples)

        nb_groups = secret_santa._get_nb_groups()

        self.assertEqual(nb_groups, 3)

    def test_get_nb_groups(self):
        people = ["Florent", "Jessica", "Ambroise",
                  "Bastien", "Coline", "Emilien"]
        couples = [("Florent", "Jessica"),
                   ("Coline", "Emilien")]
        secret_santa = SecretSanta(people, couples)

        nb_groups = secret_santa._get_nb_groups()

        self.assertEqual(nb_groups, 2)

if __name__ == '__main__':
    unittest.main()
