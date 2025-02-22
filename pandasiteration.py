student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]

}

for (key, value) in student_dict.items():
    pass
    #print(key)
    #print(value)

import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)
# Loop through a data frame
#for (key, value) in student_dataframe.items():
    #print(key)

for (index, row) in student_dataframe.iterrows():
    if row.student == "Angela":
        print(row.score)
    #print(row.student)
