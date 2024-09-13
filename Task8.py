'''Class with Highest Average: Create a dictionary
where the keys are class names, and the values are
lists of student marks. Write a function that
determines which class has the highest average marks.'''

if __name__ == "__main__":
    class_grades = {"python":[34,45,56,67,78],"PHP\t":[76,56,80,70,43],"Java":[34,45,78,7,98]}
    highest_average = 0.0
    winner_class = ""
    for class_name,marks in class_grades.items():
        total_marks = 0
        for each in marks:
            total_marks += each
            if total_marks/len(marks)> highest_average:
                winner_class = class_name
                highest_average = total_marks/len(marks)
        print(f"{class_name}\t\tclass average is {highest_average}")
    print(f"\n{winner_class}\t\thighest class average marks! {highest_average}")