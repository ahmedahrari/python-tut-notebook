#   -----------------------------------------------------------------
#                   Student Grade Recording System
#   -----------------------------------------------------------------

students = []

def add_student():
    name = input("Student Name: ").strip()
    try:
        grades = list(map(float, input("Grade (With Space): ").split()))
        if not grades:
            print("At least one score is required.")
            return
        students.append({"Name": name, "Grades": grades})
        print(f"Student '{name}'  Added.")
    except ValueError:
        print("Grades should be numbers!")

def report():
    if not students:
        print("There is no list.")
        return

    # Calculate the average of each student
    for s in students:
        s["avg"] = sum(s["grades"]) / len(s["grades"])
        s["status"] = "Pass" if s["avg"] >= 10 else "Faild"

    print("\n--- Report Card ---")
    for s in sorted(students, key=lambda x: x["avg"], reverse=True):
        print(f"{s['name']:12} | Average: {s['avg']:5.2f} | {s['status']}")
        print(f"   Grade: {s['grades']}")

    # General statistics
    all_avgs = [s["avg"] for s in students]
    print(f"\nAverage Class: {sum(all_avgs)/len(all_avgs):.2f}")
    print(f"Upper: {max(all_avgs):.2f}")
    print(f"Downer: {min(all_avgs):.2f}")

    passed = [s for s in students if s["avg"] >= 10]
    print(f"Passes: {len(passed)} from {len(students)}")

def search():
    q = input(" Searching Name: ").lower()
    matches = [s for s in students if q in s["name"].lower()]
    if matches:
        for s in matches:
            print(s)
    else:
        print("ٔNot Founded.")

while True:
    print("\n1. Add  2. Report card  3. Search  4. Exit")
    c = input("Choice: ")
    if   c == "1": add_student()
    elif c == "2": report()
    elif c == "3": search()
    elif c == "4": break