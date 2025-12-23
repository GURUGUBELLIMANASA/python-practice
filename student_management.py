#student management system using file handling
FILE_NAME= "student.txt"
def add_student();
roll = input("enter the student roll no.")
name= input("enter student name")
branch =input("enter student branch")
student = {"Roll": roll,"Name":name, "Branch": branch}
students.append(student)

def view_student();
if not student:
print("not student is found")
return

print("---student list---")
for student in students:
print{"Roll{"student['Roll']}|Name{student['name"]}|"Branch{student['branch']}"}

 def main():
 while true:
 print("---student management system---")
 print('1. add the students")
 print("2. view the students")
 print("3. exit the program")

 choice = input("enter the coice you want")

 if choice == '1':
   add student()
   elif choice == '2':
   view_student()
   elif choice =='3':
   print("exit the program")
   else
   print("invalid choice, try again")





