'''Take two lists, one containing names and
 the other containing marks. Convert them
 into a dictionary where names are keys and
  marks are values.'''

if __name__ == "__main__":
    student_names = ['ghani','khizer','sufyan','shahbaz']
    student_marks = [56, 78, 34, 98]
    student_Data = {}
    for num in range(0,len(student_names)):
        student_Data[student_names[num]] = student_marks[num]
    print(student_Data)