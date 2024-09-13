'''Create a dictionary where student names are keys
 and their marks are values. Write a function that
 finds the student with the highest marks.'''

if __name__ == "__main__":

    student_Dictionary = {'ghani': 56, 'khizer': 78, 'Sufyan': 75}
    student_marks = 0
    student_name = ''

    for _name, _marks in student_Dictionary.items():
        if student_marks < _marks:
            student_marks = _marks
            student_name = _name
    print(f"{student_name} has highest marks: {student_marks}")

