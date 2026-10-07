# =========================================================
# ΚΛΑΣΗ Student
# Αναπαριστά έναν απλό φοιτητή
# =========================================================


class Student:
    
    # Constructor της κλάσης.
    # Εκτελείται αυτόματα όταν δημιουργούμε ένα αντικείμενο Student.
    
    def __init__(self, name, student_id, grade):
        # Αποθηκεύουμε το όνομα στο αντικείμενο
        self.name = name
        # Αποθηκεύουμε τον αριθμό μητρώου
        self.student_id = student_id
        # Αποθηκεύουμε τον βαθμό
        self.grade = grade
        
    # Μέθοδος που ελέγχει αν ο φοιτητής περνάει
        
    def is_passing(self):
        if self.grade > 5:
            print("===CONGRATS! YOU PASSED===")
            
        else:
            print("===SORRY! TRY NEXT TIME===")
            
    # Μετατρέπει το αντικείμενο Student σε dictionary  
          
    def to_dict(self):
        # Επιστρέφουμε ένα dictionary
        return {
            "name": self.name,
            "student_id":self.student_id,
            "grade":self.grade
        }

# =========================================================
# ΚΛΑΣΗ GraduateStudent
# Κληρονομεί από την Student
# =========================================================
        
class GraduateStudent(Student):
     # Constructor της GraduateStudent
    def __init__(self, name, student_id, grade, thesis_name):
         # Καλούμε τον constructor της γονικής κλάσης Student
        super().__init__(name, student_id, grade)
        # Προσθέτουμε το επιπλέον attribute
        # που υπάρχει μόνο στον μεταπτυχιακό φοιτητή
        self.thesis_name = thesis_name
    
    # Override της to_dict()    
    def to_dict(self):
        # Παίρνουμε πρώτα το dictionary της Student
        data = super().to_dict()
        # Προσθέτουμε το thesis_name
        data["thesis_name"] = self.thesis_name
        # Επιστρέφουμε το ολοκληρωμένο dictionary
        return data    

    


