'''Create a list of tuples where each tuple
contains a student's name, subject, and marks.
Convert this list into a nested dictionary where
each student has a dictionary of subjects and marks.'''
if __name__ == "__main__":
    student_list = [('ghani',),("php","Python","Java"),(56,67,78)]
    updated_dictionary = {}
    student_name = list(student_list[0])
    student_subjects = list(student_list[1])
    student_marks = list(student_list[2])
    updated_dictionary['Name']=student_name[0]

    for index in range(0,len(student_subjects)):
        updated_dictionary[student_subjects[index]]=student_marks[index]
    print(updated_dictionary)








