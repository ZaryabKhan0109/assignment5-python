
students_marks={
    "Zaryab":60,
    "Jim":70,
    "Neha":80
}
z =input(" Enter student's name: ")

if z.capitalize() in students_marks.keys():
    print("{}'s marks: {}".format(z.capitalize(),students_marks[z.capitalize()]))
else:
   print("Student not found")

