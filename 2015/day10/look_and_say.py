import numpy as np
import re


def look_and_say():
    input = "1113222113"
    pattern = r"(\d)\1*"

    for i in range(0, 50):
        iterator = re.finditer(pattern, input)
        input = ""
        for match in iterator:
            input += str(len(match.group())) + match.group()[0]

    print(len(input))


if __name__ == "__main__":
    look_and_say()
