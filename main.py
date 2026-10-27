"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    """Give back what one semester costs."""
    return semester_cost


def cost_per_month(annual_cost):
    monthly_cost = annual_cost / MONTHS_PER_YEAR
    """Give back what one month of the academic year costs."""
    return monthly_cost


def cost_per_day(annual_cost):
    daily_cost = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    """Give back what one class day costs."""
    return daily_cost


def cost_per_credit(annual_cost, credits):
    credit_cost = annual_cost / (SEMESTERS_PER_YEAR * credits)
    """Give back what one credit costs. credits is the number taken this semester."""
    return credit_cost


def cost_per_class(annual_cost, credits):
    class_cost = (annual_cost / (SEMESTERS_PER_YEAR * credits)
                  * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER)
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return class_cost

def cost_per_minute(annual_cost, credits):
    minute_cost = annual_cost / (credits * CS1430_MEETINGS_PER_SEMESTER * 50)
    """Give back what one minute of a 50-minute CS 1430 class meeting costs."""
    return minute_cost
# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    annual_cost = float(input("Enter the total cost for one year: "))
    # Then ask for the credits this semester.
    credits = int(input("Enter the credits this semester: "))

    while True:
        # Show your menu here.

        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
            print(f"Cost per semester: ${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"Cost per class day: ${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per class: ${cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            print(f"Cost per minute: ${cost_per_minute(annual_cost, credits):.2f}")
        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
