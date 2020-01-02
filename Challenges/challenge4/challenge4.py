
import unittest

from fibonacci import *


class Challenge4(unittest.TestCase):

    def test_challenge4(self):
        print(convert_number_to_string(Fibonacci(32)))


if __name__ == '__main__':
    unittest.main()


def convert_number_to_string(number):
    description = ""
    scale_index = 0
    orig_number = number
    if number == 0:
        description = "zero"
    else:
        while number > 0:
            # do the smallest scale first and prepend the larger scales
            description = convert_number_less_than_1000(number % 1000) + scale[scale_index] + description
            number = number / 1000
            scale_index = scale_index + 1

    return str(orig_number) + " - " + description


def convert_number_less_than_1000(number):
    hundreds_index = 0
    if number >= 1000:
        return "error: " + str(number) + "is not in range for this function"
    else:
        hundreds_index = number / 100
    description = ""
    if hundreds_index > 0:
        description = str(zeroToTwenty[hundreds_index]) + " hundred "
    # else, the hundreds are still blank.
    return description + convert_number_less_than_100(number % 100)


def convert_number_less_than_100(number):
    ten_index = 0
    teen_index = 0
    if number >= 100:
        return "error: " + str(number) + "is not in range for this function"
    else:
        ten_index = number / 10
        if ten_index > 1:
            mod_val = 10
        else:
            mod_val = 20
        teen_index = number % mod_val
    # print (ten_index)
    # print (teen_index)
    return tens[ten_index] + " " + zeroToTwenty[teen_index]


zeroToTwenty = ["",
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
                "ten",
                "eleven",
                "twelve",
                "thirteen",
                "fourteen",
                "fifteen",
                "sixteen",
                "seventeen",
                "eighteen",
                "nineteen",
                "twenty"]

tens = ["",
        "",
        "twenty ",
        "thirty ",
        "fourty ",
        "fifty ",
        "sixty ",
        "seventy ",
        "eighty ",
        "ninety "]

scale = [" ",
         " thousand ",
         " million ",
         " billion ",
         " trillion "]
