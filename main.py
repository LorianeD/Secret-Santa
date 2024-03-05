from secretsanta.data import PEOPLE, COUPLES
from secretsanta.tui import home_menu, exit_message
from secretsanta.secret_santa import SecretSanta
from secretsanta.distribution_verification import is_gifts_valid


def main() -> None:
    """The main function for the Secret Santa application."""
    # Get people distribution
    santa = SecretSanta(PEOPLE, COUPLES)
    distribution = santa.compute_distribution()
    if not is_gifts_valid(PEOPLE, COUPLES, distribution):
        print("Une erreur est survenue lors de la selection des pères noël.")
        exit(1)

    # Display user menu
    try:
        home_menu(PEOPLE, distribution)
    except KeyboardInterrupt:
        exit_message()


if __name__ == "__main__":
    main()
