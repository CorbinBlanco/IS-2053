def calc_average(s1, s2, s3, s4, s5, s6, s7, s8):
    average = (s1+s2+s3+s4+s5+s6+s7+s8) / 8
    return average

def determine_grade(score):
    if 98 <= score <= 100:
        return "A+"
    if 92 <= score <= 98:
        return "A"
    if 90 <= score <= 92:
        return "A-"
    if 88 <= score <= 90:
        return "B+"
    if 82 <= score <= 88:
        return "B"
    if 80 <= score <= 82:
        return "B-"
    if 78 <= score <= 80:
        return "C+"
    if 72 <= score <= 78:
        return "C"
    if 70 <= score <= 72:
        return "C-"
    if 68 <= score <= 70:
        return "D+"
    if 62 <= score <= 68:
        return "D"
    if 60 <= score <= 62:
        return "D-"
    if score < 60:
        return "F"


def main():

    s1N = int(input("Enter score 1: "))
    s1L = determine_grade(s1N)

    s2N = int(input("Enter score 2: "))
    s2L = determine_grade(s2N)

    s3N = int(input("Enter score 3: "))
    s3L = determine_grade(s3N)

    s4N = int(input("Enter score 4: "))
    s4L = determine_grade(s4N)

    s5N = int(input("Enter score 5: "))
    s5L = determine_grade(s5N)

    s6N = int(input("Enter score 6: "))
    s6L = determine_grade(s6N)

    s7N = int(input("Enter score 7: "))
    s7L = determine_grade(s7N)

    s8N = int(input("Enter score 8: "))
    s8L = determine_grade(s8N)

    print()
    print("Score\t\tNumeric Grade\tLetter Grade")
    print("----------------------------------------------------")

    print(f"score 1:\t\t{s1N:.1f}\t\t\t{s1L}")
    print(f"score 2:\t\t{s2N:.1f}\t\t\t{s2L}")
    print(f"score 3:\t\t{s3N:.1f}\t\t\t{s3L}")
    print(f"score 4:\t\t{s4N:.1f}\t\t\t{s4L}")
    print(f"score 5:\t\t{s5N:.1f}\t\t\t{s5L}")
    print(f"score 6:\t\t{s6N:.1f}\t\t\t{s6L}")
    print(f"score 7:\t\t{s7N:.1f}\t\t\t{s7L}")
    print(f"score 8:\t\t{s8N:.1f}\t\t\t{s8L}")
    print("----------------------------------------------------")

    print(f"Average of all the scores for the course is a {calc_average(s1N, s2N, s3N, s4N, s5N, s6N, s7N, s8N):.1f} %.")



    averageL = determine_grade(calc_average(s1N, s2N, s3N, s4N, s5N, s6N, s7N, s8N))
    print(f"The letter grade for the course is a '{averageL}'.")


if __name__ == "__main__":
    main()