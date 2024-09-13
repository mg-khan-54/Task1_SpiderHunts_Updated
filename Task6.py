'''Create a dictionary with student names as keys
and their marks as values. Write a function to calculate
 and return the average marks of all students.'''


def students(student_Dict):
    '''This function takes dictionary as argument of student names and marks,
and returns average of all students marks'''
    total_marks = 0
    for name, marks in student_Dict.items():
        total_marks += marks
    print(total_marks / len(student_Dict))


if __name__ == "__main__":
    def main():
        student_dictionary = {"ghani": 56, "sufyan": 45, "khizer": 78, "shahbaz": 34}
        students(student_dictionary)
        # print(students.__doc__)


    main()
