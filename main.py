# Εισαγωγή των κλάσεων από το custom module
from models import Student, GraduateStudent

# Built-in module για JSON
import json


# Λίστα όλων των φοιτητών
students = []


graduate = GraduateStudent("Γιώργος Αλεξανδρίδης", 346709, 8, "A.I.")
students.append(graduate)

# =========================================================
# ΣΥΝΑΡΤΗΣΗ ΚΑΤΑΧΩΡΗΣΗΣ ΦΟΙΤΗΤΗ
# =========================================================

def add_student():

    # Εισαγωγή στοιχείων
    name = input("Ονοματεπώνυμο: ")
    student_id = int(input("Α.Μ.: "))
    grade = float(input("Βαθμός: "))

    # Δημιουργία αντικειμένου Student
    student = Student(name, student_id, grade)

    # Προσθήκη στη λίστα
    students.append(student)

    print("Ο φοιτητής καταχωρήθηκε επιτυχώς.")


# =========================================================
# ΣΥΝΑΡΤΗΣΗ ΠΡΟΒΟΛΗΣ ΦΟΙΤΗΤΩΝ
# =========================================================

def view_students():

    # Έλεγχος αν υπάρχουν φοιτητές
    if len(students) == 0:

        print("Δεν υπάρχουν καταχωρημένοι φοιτητές.")
        return

    # Άθροισμα βαθμών
    total = 0

    # Επανάληψη για όλους τους φοιτητές
    for student in students:

        print(
            f"Όνομα: {student.name} | "
            f"Α.Μ.: {student.student_id} | "
            f"Βαθμός: {student.grade}"
        )

        # Αυτόματος έλεγχος προαγωγής
        student.is_passing()

        # Προσθήκη βαθμού στο άθροισμα
        total += student.grade

    # Υπολογισμός μέσου όρου
    average = total / len(students)

    print(f"\nΜέσος όρος τμήματος: {average:.2f}")

    # Μετατροπή Student objects σε dictionaries
    data = [student.to_dict() for student in students]

    # Μετατροπή σε JSON
    print("\nJSON:")
    print(json.dumps(data, indent=4, ensure_ascii=False))


# =========================================================
# ΚΥΡΙΟ MENU
# =========================================================

while True:

    print("\n===== ΗΛΕΚΤΡΟΝΙΚΗ ΓΡΑΜΜΑΤΕΙΑ =====")
    print("1. Καταχώρηση νέου φοιτητή & βαθμολογίας")
    print("2. Προβολή όλων των φοιτητών & υπολογισμός μέσου όρου")
    print("3. Τερματισμός")

    # Επιλογή χρήστη
    choice = input("Επιλέξτε: ")

    # Επιλογή 1
    if choice == "1":

        add_student()

    # Επιλογή 2
    elif choice == "2":

        view_students()

    # Επιλογή 3
    elif choice == "3":

        print("Έξοδος από την εφαρμογή.")
        break

    # Άλλη επιλογή
    else:

        print("Μη έγκυρη επιλογή.")