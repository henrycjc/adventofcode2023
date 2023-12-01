def get_data() -> list[str]:
    data = """sixsrvldfour4seven
    snip snip"""
    return [row.strip() for row in data.split("\n")]


if __name__ == "__main__":

    def day1():
        data = get_data()
        total = 0
        for row in data:
            row_vals = []
            for c in row:
                if c.isdigit():
                    row_vals.append(c)
            first = row_vals[0]
            last = row_vals[-1]
            print(
                f"{row} contains {row_vals} which has first val {row_vals[0]} and last val {row_vals[-1]} for total {first + last}"
            )
            val = int(f"{first + last}")
            total += val
        print(total)

    # day1()

    import re

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
            match: re.Match
            for match in re.findall(
                r"one|two|three|four|five|six|seven|eight|nine|ten|\d", row
            ):
                match_str = str(match)
                if match_str.isdigit():
                    row_vals.append(int(match_str))
                else:
                    row_vals.append(digit_map[match_str])
            first = row_vals[0]
            last = row_vals[-1]
            print(
                f"{row} contains {row_vals} which has first val {row_vals[0]} and last val {row_vals[-1]} for total {str(first) + str(last)}"
            )
            val = int(f"{str(first) + str(last)}")
            total += val
        print(total)

    day1_question2()
