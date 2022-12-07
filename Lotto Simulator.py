from random import randint, sample, shuffle


def main():
    count = 6
    winning_set = randomize_winning_set(count)
    user_set = take_user_input(count)
    correct_guesses = 0
    print(winning_set)
    print(user_set)


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
    """Takes input from user, and makes a list of theirs guessed numbers.

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
            user_set.append(num)
            guess += 1
        except ValueError:
            print('This is not a valid entry!')
    return sorted(user_set)





if __name__ == '__main__':
    main()
