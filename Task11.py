'''You have 3 dictionaries, each representing different
subjects and their corresponding marks for students.
Write a program to merge these dictionaries into one
where each student has their total marks from all subjects.'''

student_1 = [{"Name": "Ghani"}, {"python": 34}, {"PHP": 23}, {"Java": 28}]
student_2 = [{"Name": "Khizer"}, {"python": 76}, {"PHP": 34}, {"Java": 65}]
student_3 = [{"Name": "Sufyan"}, {"python": 78}, {"PHP": 38}, {"Java": 73}]
merged_dictionary = {}


def student(student_list):
    '''student function that takes a list of dictionaries as input of student data
and returns a dictionary with each student total marks'''
    student_name = ''
    total_marks = 0
    for index in student_list:
        for key, value in index.items():
            if key == "Name":
                student_name = value
            else:
                total_marks += value
        merged_dictionary[student_name] = total_marks


def main():
    student(student_1)
    student(student_2)
    student(student_3)
    print(merged_dictionary)

    # print(student.__doc__)


if __name__ == "__main__":
    main()
