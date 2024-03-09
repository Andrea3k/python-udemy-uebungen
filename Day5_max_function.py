student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

highest_score = 0
for student_score in student_scores: 
     if student_score > highest_score: 
        highest_score = student_score
    
print(f"The highest score in the class is: {highest_score}")