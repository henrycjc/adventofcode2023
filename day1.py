import re


def get_data() -> list[str]:
    with open("day1_input.txt", mode="r") as file:
        return [row.strip() for row in file]


if __name__ == "__main__":

    def day1():
        data = get_data()
        total = 0
        for row in data:
            row_vals = [c for c in row if c.isdigit()]
            total += int(f"{row_vals[0] + row_vals[-1]}")
        assert total == 54561, "Day1, Q1 wrong"
        print(total)

    day1()

    def day1_question2():
        data = get_data()
        total = 0
        digit_map = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        for row in data:
            row_vals = []
            for match in re.findall(
                r"one|two|three|four|five|six|seven|eight|nine|ten|\d", row
            ):
                if match.isdigit():
                    row_vals.append(int(match))
                else:
                    row_vals.append(digit_map[match])
            total += int(f"{str(row_vals[0]) + str(row_vals[-1])}")
        assert total == 54076, "Day1,Q2"
        print(total)

    day1_question2()
