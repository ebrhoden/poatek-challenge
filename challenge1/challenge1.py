MINIMUM_AGE = 13
HEIGHT_INDEX = 1
AGE_INDEX = 2


def count_how_many_values_below_some_value(list_of_values, some_value):
    counter = 0

    for value in list_of_values:
        if value < some_value:
            counter += 1

    return counter


if __name__ == '__main__':
    # Example provided in the challenge
    students = [
        ["Bruno", 170, 14],
        ["Leonardo", 174, 21],
        ["Juan", 156, 12],
        ["Juliana", 166, 13],
        ["Wagner", 184, 17],
        ["Micaela", 172, 18],
        ["Bento", 150, 14],
        ["Lucia", 162, 13],
        ["Pedro", 169, 14],
        ["Carla", 158, 16]
    ]

    sum_height = 0
    average_height = 0

    list_heights_students_above_minimum_age = []

    # Calculating the sum of heights and creating a list of students above the minimum age in the same loop
    for student in students:
        sum_height += student[HEIGHT_INDEX]
        if student[AGE_INDEX] > MINIMUM_AGE:
            list_heights_students_above_minimum_age.append(student[HEIGHT_INDEX])

    average_height = sum_height / len(students)

    # The desired value is stored in the variable below
    number_students_over_minimum_age_and_below_average_height = count_how_many_values_below_some_value(
        list_heights_students_above_minimum_age,
        average_height)

    print(f"Number of students over {MINIMUM_AGE} who are below average height: "
          f"{number_students_over_minimum_age_and_below_average_height}")

