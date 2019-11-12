#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: november 2019
# This program will allow you to multiply one number to the power of another


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    # This is what runs the program.
    print("")
    print("This program will allow you to multiply one number to the power"
          " of another...")
    print('')

    while True:
        # Input
        number_as_string = input(color.BOLD + color.YELLOW + 'Input a number: '
                                 + color.END)
        power_as_string = input(color.BOLD + color.YELLOW + 'Input a number to'
                                ' multiply to the power of (must be a positive'
                                + ' and whole number): ' + color.END)

        next_full_number = 0
        number_total = 1

        # Process
        try:
            number = int(number_as_string)
            power = int(power_as_string)

            if power > 0:
                while next_full_number < power:
                    next_full_number = next_full_number + 1
                    number_total = number_total * number

                print(color.GREEN + 'The answer is {0}'.format(number_total)
                      + color.END)
                break

            else:
                print('')
                print(color.PURPLE + color.UNDERLINE + 'That is not a positive'
                      ' and/or whole number...' + color.END)
                print("")
                print("")

        # This stops them from putting in something let bob and gets them to
        # re-input their age.
        except Exception:
            print('')
            print(color.PURPLE + color.UNDERLINE + 'That is not a positive'
                  ' and/or whole number...' + color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
