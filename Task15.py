"""Create a dictionary where student names are keys
and marks are values. Write a function that returns
the names of the top 3 students based on their marks."""
if __name__ == "__main__":

    student_marks_sheet = {'Ghani': 85, 'Khizer': 175, 'Sufyan': 189, 'Shahbaz': 78, 'Danial': 115, 'giku': 145}
    temp_mark_sheet = student_marks_sheet
    highest_temp = 0
    highest_mark = {}
    name_temp = ''
    for index in range(len(student_marks_sheet)):
        if len(highest_mark) == 3:
            continue
        for item_name, item_marks in temp_mark_sheet.items():
            if item_marks > highest_temp:
                name_temp = item_name
                highest_temp = item_marks
        highest_mark[name_temp] = highest_temp
        highest_temp = 0
        del temp_mark_sheet[name_temp]

    print(highest_mark)
