"""Create a dictionary of students and their marks.
 Write a function that removes all students whose marks
  are below the average marks of the class."""


if __name__ == "__main__":
    student_marksheet = {'Ghani': 85, 'Khizer': 175, 'Sufyan': 189}
    print(student_marksheet)
    class_average = 0.0
    Updated_list = []
    total_marks = 0
    for name, marks in student_marksheet.items():
        total_marks += marks
        class_average = total_marks/len(student_marksheet)
    print(f"average of the class is {class_average}")

    for name, marks in student_marksheet.items():
        if marks < class_average:
            Updated_list.append(name)
    for index in range(0, len(Updated_list)):
        del student_marksheet[Updated_list[index]]
    print(student_marksheet)
