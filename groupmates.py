#coding: utf-8
groupmates = [
	{
		"name": ("Иван"),
		"group": "1702",
		"age": 20,
		"marks": [3, 4, 4, 5, 4]
	},
	{
		"name": ("Владлена"),
		"group": "1702",
		"age": 19,
		"marks": [4, 5, 3, 4, 3]
	},
	{
		"name": ("Татьяна"),
		"group": "1701",
		"age": 19,
		"marks": [3, 3, 3, 3, 4]
	},
	{
		"name": ("Александр"),
		"group": "1701",
		"age": 20,
		"marks": [4, 4, 5, 5, 5]
	}
	]

def print_students(students):
	print (("Имя студента").ljust(15),	\
		("Группа").ljust(8),	\
		("Возраст").ljust(8),	\
		("Оценки").ljust(20))
	for student in students:
		print (student["name"].ljust(15),	\
			student["group"].ljust(8),	\
			str(student["age"]).ljust(8),	\
			str(student["marks"]).ljust(20))
	print ("\n")
print_students(groupmates)

def students_avg(students, n):
   
 
    return [s for s in students if sum(s['marks'])/len(s['marks']) > n]
 

print()
print_students(students_avg(groupmates, 4))
