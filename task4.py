"""Create a dictionary of students and their marks.
 Write a function that takes a student’s name and
  updates their marks if they exist in the dictionary;
  otherwise, it adds the student with the new marks."""

if __name__ == "__main__":
    students_Dictionary = {'Ghani': 56, 'Khizer': 78, 'Sufyan': 34, 'Shahbaz': 98}
    student_name = input('Enter student name: ')
    print(students_Dictionary)

    for name, marks in students_Dictionary.items():
        if name == student_name:
            print(f"15 Marks Awarded to {name}")
            students_Dictionary[name] = marks + 15
    print(students_Dictionary)
