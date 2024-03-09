student_heights = input().split()

# Amount of students
for n in range(0, len(student_heights)): 
    student_heights[n] = int(student_heights[n])

number_students = 0
for n in student_heights: 
    number_students = number_students + 1 
print("number of students: ", number_students)

# Sum student height
sum_height = 0
for student_height in student_heights: 
    sum_height = sum_height + student_height
print("total height: ", sum_height)

# average height of students
average_height = int(round(sum_height/number_students, 0))
print("average height: ", average_height)

# test numbers 156 178 165 171 187