"""
Student Grade Calculator
Week 2 Python Project
"""

def get_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.\n")

        except ValueError:
            print("❌ Please enter a valid number.\n")


def calculate_grade(marks):

    if marks >= 90:
        return "A", "Outstanding! Excellent work! 🌟"

    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"

    elif marks >= 70:
        return "C", "Good Job! You can do even better! 😊"

    elif marks >= 60:
        return "D", "Keep Practicing! Improvement is possible! 💪"

    else:
        return "F", "Don't Give Up! Try Again! ❤️"


def display_result(name, marks, grade, message):

    print("\n" + "=" * 40)
    print(f"RESULT FOR {name.upper()}")
    print("=" * 40)

    print(f"Marks : {marks}/100")
    print(f"Grade : {grade}")
    print(f"Message : {message}")

    print("=" * 40)


def main():

    print("=" * 45)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 45)

    name = input("Enter Student Name: ")

    marks = get_marks()

    grade, message = calculate_grade(marks)

    display_result(name, marks, grade, message)


if __name__ == "__main__":
    main()
