import sys


def get_user_input() -> str:
    """This fucntion return user input

    Returns:
        string: user input string
    """
    data = input("What is the text to count?\n")
    return data


def calculate_data(user_input, spaces=0) -> str:
    """laverage the sum of chars based on the user_input

    Args:
        user_input (string): user written input
        spaces (int, optional): number of spaces. Defaults to 0.
    """
    upper_sum = lower_sum = char_sum = 0
    spaces_sum = spaces
    punctuation_sum = digits_sum = 0

    for char in user_input:
        if char.isalpha() and char.isupper():
            upper_sum += 1
        elif char.isalpha() and char.islower():
            lower_sum += 1
        elif char.isspace():
            spaces_sum += 1
        elif char.isdigit():
            digits_sum += 1
        else:
            punctuation_sum += 1
        char_sum += 1
    print(f"The text contains {char_sum} characters:")
    print(f"{upper_sum} upper letters")
    print(f"{lower_sum} lower letters")
    print(f"{punctuation_sum} punctuation marks")
    print(f"{spaces_sum} spaces")
    print(f"{digits_sum} digits")


def main():
    """main fuction
    """
    if len(sys.argv) > 2:
        print("AssertionError")
        return
    if (len(sys.argv) != 2):
        spaces = 0
        while (True):
            spaces += 1
            data = get_user_input()
            if (data != ""):
                break
    else:
        data = sys.argv[1]
    output = calculate_data(data, spaces)
    print(output)


if __name__ == "__main__":
    main()
