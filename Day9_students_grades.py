student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for n in student_scores: 
    if student_scores[n] > 100 or student_scores[n] < 0: 
        student_grades[n] = "CHEATED!"
    elif student_scores[n] >= 91: 
        student_grades[n] = "Outstanding"
    elif student_scores[n] >= 81:
        student_grades[n] = "Exceeds Expactations" 
    elif student_scores[n] >= 71: 
        student_grades[n] = "Acceptable"
    elif student_scores[n] < 70 and student_scores[n] >= 0: 
        student_grades[n] = "Fail"

print(student_grades)