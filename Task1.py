"""Write a program to store information about 5 students
 (name, roll number, and marks) using a list of dictionaries.
  Each dictionary should represent one student."""
class Student:
    def user_input(self):
        """user input function gets the data from user
and returns a dictionary of student data."""
        student_dict = {}
        student_name = input(f'Enter student name: ')
        roll_number = input(f'Enter roll number: ')
        marks = input('Enter marks: ')
        student_dict['name'] = student_name
        student_dict['roll Number'] = roll_number
        student_dict['marks'] = marks
        return student_dict


    def print_data(self, dictionary_Student):
        """This function takes Student dictionary as argument
and prints the data with formating"""
        print(dictionary_Student["name"],"\t", dictionary_Student["roll Number"],"\t",dictionary_Student["marks"])

def main():
    # for x in range(6):
    student_1, student_2, student_3, student_4, student_5 = Student(), Student(), Student(), Student(), Student()
    object_list = [student_1, student_2, student_3, student_4, student_5]
    return_list = []
    for instance in object_list:
        return_list.append(instance.user_input())
    print(Student.user_input.__doc__)
    index = 0
    for instance in object_list:
        instance.print_data(return_list[index])
        index += 1
    print(Student.print_data.__doc__)


    # student_1 = Student()
    # student_2 = Student()
    # student_3 = Student()
    # student_4 = Student()
    # student_5 = Student()
    # student_6 = Student()
    # student_7 = Student()

    # student_1_p = student_1.data_entry()
    # student_2_p = student_2.data_entry()
    # student_3_p = student_3.data_entry()
    # student_4_p = student_4.data_entry()
    # student_5_p = student_5.data_entry()
    # student_6_p = student_5.data_entry()
    # student_7_p = student_5.data_entry()
    #
    # student_1.print_data(student_1_p)
    # student_2.print_data(student_2_p)
    # student_3.print_data(student_3_p)
    # student_4.print_data(student_4_p)
    # student_5.print_data(student_5_p)
    # student_6.print_data(student_5_p)
    # student_7.print_data(student_5_p)

if __name__ == "__main__":
    main()
