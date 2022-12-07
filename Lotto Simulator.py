from random import sample, shuffle


def main():
    count = 6
    winning_set = randomize_winning_set(count)
    user_set = take_user_input(count)
    correct_guesses = compare_lists(winning_set, user_set)

    print('')
    print(f'Your numbers: {user_set}')
    print(f'Winning numbers: {winning_set}')
    print(f'Correct guesses: {correct_guesses[1]}')
    print('')

    if correct_guesses[0] == 0:
        print('Unfortunately, you did not guess any of the numbers :( ')
    elif correct_guesses[0] == 1:
        print(f'Congratulations! You guessed 1 number!')
    elif 6 > correct_guesses[0] > 1:
        print(f'Congratulations! You guessed {correct_guesses[0]} numbers!')
    else:
        print('It is UNBELIEVABLE!! You guessed all of the numbers! You win the main price!')


def randomize_winning_set(count):
    """Generate given amount of random numbers between 0 and 49.

    :param count: an integer that states how many numbers are to be generated.
    :return: a list containing a set of number of length of 'count' parameter.
    """

    num_list = list(range(1, 50))
    shuffle(num_list)
    num_set = sorted(sample(range(1, 50), count))
    return num_set


def take_user_input(count):
    """Takes input from user, and makes a list of their guessed numbers.

    :param count: an integer that states how many numbers are to be generated.
    :return: a list containing users' input
    """

    user_set = []
    guess = 1
    while guess < count + 1:
        try:
            num = int(input(f'{guess}: Choose a number from 1 to 49: '))
            if num < 1 or num > 49:
                raise ValueError
            elif num in user_set:
                print('You have already chosen that number!')
                raise ValueError
            user_set.append(num)
            guess += 1
        except ValueError:
            print('This is not a valid entry!')
            print('')
    return sorted(user_set)


def compare_lists(list_1, list_2):
    """Check how many values are shared by two different lists.

    :param list_1: first set of values
    :param list_2: second set of values
    :return: an integer: a number of values that repeat for both lists,
            a list of numbers that repeated
    """

    repeats = 0
    repeats_list = []
    for i in list_1:
        if i in list_2:
            repeats += 1
            repeats_list.append(i)
    return repeats, repeats_list


if __name__ == '__main__':
    main()
