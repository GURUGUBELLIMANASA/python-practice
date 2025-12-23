#student management system using file handling
students = []
def add_student():
    roll = input("Enter the student roll no.")
    name = input("Enter student name")
    branch = input("Enter student branch")
    student = {"Roll": roll,"Name": name, "Branch": branch}
    students.append(student)

def view_students():
  if not students:
      print("not student is found")
      return

  print("---Student list---")
  for student in students:
        print(f"Roll:{student["Roll"]}|Name:{student["name"]}|Branch:{student["branch"]}")
      print()

def main():
  while True:
      print("---student management system---")
      print("1. add the student")
      print("2. view the studens")
      print("3. exit the program")

      choice = input("enter the coice you want: ")

      if choice == "1":
        add student()
      elif choice == "2":
        view_student()
      elif choice =="3:
        print("exit the program")
        break
      else:
        print("invalid choice, try again")
main()




