#List Comprehension

# range = range(1,5)
#
# new_list = [n*2 for n in range if n%2 == 0]
#
# print(new_list)

#Dictionary Comprehension
# import random
#
# names = ['Alex','Bob']
#
# students_scores = {student:random.randint(0,100) for student in names}
# passed_students = {student:score for (student,score) in students_scores.items() if score > 60}
# print(passed_students)

#DataFrame Comprehension

# import pandas
#
# student_dict = {
#     "student": ["Kevin", "Bob", "Mike"],
#     "score": [50, 70, 90]
# }
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# #Loops through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)