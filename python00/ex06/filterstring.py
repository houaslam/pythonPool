from ft_filter import ft_filter
import sys

def ft_filterString(stringInput: str, charNum: int):
    return ft_filter(lambda x: len(x) >= charNum, stringInput.split(" "))


if __name__ == "__main__":
    try:
        data = sys.argv[1]
        char_int = int(sys.argv[2])
        print(list(ft_filterString(data, char_int)))
    except Exception as e:
        print("AssertionError: the arguments are bad")
