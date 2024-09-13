"""Create a list of dictionaries where each
 dictionary contains a student’s name and
 their marks. Sort the list by marks in descending order."""

if __name__ == "__main__":
    students_list = [{"Ghani": 56}, {"Sufyan": 45}, {"Khizer": 78}, {"Shahbaz": 34}]
    temp_list = students_list.copy()
    temp_mark = 0
    temp_name = ""
    newStudent = []
    for num in range(len(temp_list)):
        for list_item in students_list:
            for name, marks in list_item.items():
                # print(a,"and", b)
                if temp_mark < marks:
                    temp_mark = marks
                    index_value = list_item
        newStudent.append(index_value)
        temp_mark = 0
        students_list.remove(index_value)
    students = temp_list
    print(newStudent)
