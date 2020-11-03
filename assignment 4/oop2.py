class Student_score:
    def student_scores(self):
        STA = "A1"
        MTHS = "B2"
        COM = "A1"
        print(f" {name}these are your scores STA:{STA}, MTHS:{MTHS}, COM:{COM}.")

class Amaka(Student_score):
    pass

class John(Student_score):
   pass

name = Amaka()
name.student_scores() 


name = John()
name.student_scores()
          
