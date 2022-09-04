from random import randint


def get_user_number():
    while True:
        try:
            user_number = int(input("Guess the number between 1 and 100: "))
            break
        except ValueError:
            print("It's not a number!")

    return user_number


def get_draw_number():
    draw_number = randint(1, 100)
    user_number = get_user_number()

    while user_number != draw_number:
        if user_number > draw_number:
            counter += 1
            print("Too big!")
        elif user_number < draw_number:
            counter += 1
            print("Too small!")
        user_number = get_user_number()
    print("You win!")


if __name__ == '__main__':
    get_draw_number()
