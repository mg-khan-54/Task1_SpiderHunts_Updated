"""Write a program that takes a list of student marks
 and counts how many times each mark appears using a dictionary.
"""
if __name__ == "__main__":

    student_data = {}
    marks_list = []
    final_result = {}
    counter = 0
    index = 0
    input_name = input("Enter your name: ")

    for x in range(0, 10):
        input_marks = int(input('Enter marks: '))
        marks_list.append(input_marks)  #creats marks list form user input
    student_data[input_name] = marks_list  #creates dictionary with name as key and marks list as value
    print(student_data)

    for name, mark_list in student_data.items():
        for mark in mark_list:
            value = mark
            for index_ in range(len(mark_list)):
                if value == mark_list[index_]:
                    counter += 1
                final_result[mark] = counter
                index += 1
            counter = 0
    print(final_result)
