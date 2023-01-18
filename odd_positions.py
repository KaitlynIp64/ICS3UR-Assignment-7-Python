#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Jan 2023
# This program prints the odd numbers in a list

import random


def find_odd_positions(list_of_numbers):
    # this function prints the odd numbers

    odd_numbers = []
    loop_counter = 1

    for list_item in list_of_numbers:
        if loop_counter % 2 != 0:
            odd_numbers.append(list_item)
        loop_counter += 1

    return odd_numbers


def main():
    # this function creates random numbers in a list

    list_of_numbers = []

    # input, process & output
    n_num_of_elements = input("# of random numbers you want: ")

    try:
        num_of_elements = int(n_num_of_elements)
        if num_of_elements > 0:
            for loop_counter in range(0, num_of_elements):
                random_num = random.randint(1, 100)  # a number between 1-100
                list_of_numbers.append(random_num)
                print(
                    "The random number {0} is : {1}".format(
                        loop_counter + 1, random_num
                    )
                )
                loop_counter += 1

            odd_numbers = find_odd_positions(list_of_numbers)

            print("\nThe numbers in odd positions in the list are : ", end="")
            for list_item in odd_numbers:
                print("{0} ".format(list_item), end="")
        else:
            print("\nThat is a negative input.")
    except ValueError:
        print("\nThat is not a valid input.")

    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
