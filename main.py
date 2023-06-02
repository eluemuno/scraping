from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Odidama", 'https://en.wikipedia.org/wiki/', 'Albert Einstein')


def introduce_yourself():
    robot.say_hello()


def show_first_paragraph():
    robot.get_first_paragraph()


def get_birth_death_dates_and_age():
    robot.get_birth_death_dates()


def say_goodbye():
    robot.say_goodbye()


def main():
    try:
        introduce_yourself()
        show_first_paragraph()
        get_birth_death_dates_and_age()
    finally:
        say_goodbye()


if __name__ == "__main__":
    main()
