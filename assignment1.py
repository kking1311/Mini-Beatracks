def option2(course_list,enrollment_list,student_list): # this function executes every case with respect to option 2 
    studentID=int(input("Enter your student ID : "))
    try:
      valid=validity(student_list,studentID)
      if valid==False:
        print(f"The student ID is invalid !!")
      else:
        print("You've chosen to to enroll into a course !!!")
        subject=input("Enter the course that you want to enroll in .")
        if isFull(course_list,subject):
          print(f"The course is already full !!!")
        elif alreadyRegistered(studentID,subject,enrollment_list):
          print(f"The course {subject} is already registered in , you cannot register")
        elif isAlreadyRegistered(enrollment_list,course_list,studentID,subject):
          print(f"you have registered in another course at the same time .")
        elif subjectCorrect(course_list,subject)==False:
          print(f"The subject {subject} you wanted to enroll in , does not exist !!")
        else:
          student_details=enrollment_list[studentID]
          student_details.append(subject)
          enrollment_list[studentID]=student_details
          subj_detail=course_list[subject]  # decreasing the value of the seats after it has been enrolled
          sub_capacity=subj_detail[1]
          sub_capacity-=1
          subj_detail[1]=sub_capacity
          course_list[subject]=subj_detail
          print("The new course list is as follows :")
          for i in student_details:
           print(f">{i}")
    except ValueError:
       print("Invalid student ID !!")

def isFull(courses_list,sub):# checks if the course is full or not
   course_detail=courses_list[sub]
   course_vacancy=course_detail[1]
   if course_vacancy==0:
      return True
   return False

def alreadyRegistered(ID,sub,enrollment_list): #checks if the user is already enrolled and is trying to enroll it again
   stud=enrollment_list[ID]
   if sub in stud:
      return True
   else:
      return False
   
def isAlreadyRegistered(enrollment_list,courses_list,ID,sub): # checks if the student is regotered in another course at the sametime
   if ID in enrollment_list:
        student_courses = enrollment_list[ID]
        course_details = courses_list.get(sub)
        if course_details is None:
            return False  # Course does not exist in the courses list
        course_timing = course_details[0]
        for enrolled_course in student_courses:
            enrolled_course_details = courses_list.get(enrolled_course)
            if enrolled_course_details is None:
                continue  # Skip invalid courses in the student's enrollment list
            enrolled_course_timing = enrolled_course_details[0]
            if enrolled_course_timing == course_timing:
                return True  # Student is already registered in a course at the same time
   return False

def subjectCorrect(courses_list,sub):# check if the course entered is correct or not
   if sub in courses_list.keys():
      return True
   else:
      return False

def validity(student_list,ID): # checking the validity of the student ID entered
   if ID in student_list:
      return True
   else:
      return False
   
def option3(enrollmentList,student_list,courses_list): #checks for cases for option 3
   studentID=int(input("Enter your student ID : "))
   valid=validity(student_list,studentID)
   if valid==False:
      print(f"The student ID is invalid !!")
   else:
      print("You've chosen to to drop into a course !!!")
      stud=enrollmentList[studentID]
      print("Select the courses that you want to drop !!")
      for i in stud:
         print(i)
      subject=input("Enter the course that you want to drop.")
      if subjectCorrect(courses_list,subject)==False:
         print(f"The subject is not in the list .")
      else:
         drop(courses_list,enrollmentList,studentID,subject)

def drop(courses_list,enrollmentList,ID,sub):# drops the desired course
   student_details=enrollmentList[ID]
   ind=student_details.index(sub)
   del student_details[ind]
   enrollmentList[ID]=student_details
   print(f"You've dropped {sub} !!")
   subj_detail=courses_list[sub]  # increasing the value of the seats after it has been dropped
   sub_capacity=subj_detail[1]
   sub_capacity+=1
   subj_detail[1]=sub_capacity
   courses_list[sub]=subj_detail
   print("The new course list is as follows:")
   for i in student_details:
      print(f">{i}")
# prints the menu
def options():
   print("                          ")
   print("==========================")
   print("Welcome to Mini-BearTracks")
   print("==========================")
   print("")
   print("What would you like to do?")
   print("1. Print timetable")
   print("2. Enroll in course")
   print("3. Drop course")
   print("4. Quit")


"""{'CMPUT 101': ['TR 14:00', 156, 'Marianne Morris'], ...."""
def courses():
 course_dict = {}
 with open("C:\\Users\\hp\\Downloads\\courses.txt", "r") as file:
    for line in file:
        parts = line.strip().split('; ')
        if len(parts) >= 4:  # Check if the line contains at least four parts
            course_code = parts[0]
            time = parts[1]
            max_students = int(parts[2])
            prof = parts[3]
            course_details = [time, max_students, prof]
            course_dict[course_code] = course_details
 return course_dict

def enrollment():
 with open("C:\\Users\\hp\\Downloads\\enrollment.txt", 'r') as f:
    lines = f.read().splitlines()
 enrollment_dict = {}
 for line in lines:
   pairs= line.split(':')
   key=int(pairs[1])
   value=pairs[0].strip()
   if key in enrollment_dict:
        enrollment_dict[key].append(value)
   else:
        enrollment_dict[key] = [value]
 return enrollment_dict

def student_info():

   """reads all the text from the file 'students.txt'
   and converts it into a dictionary with the student ID as the key and the rest as values.
   The returned dictionary is as follows:

   {181260: ['SCI', 'Cher']}, 123456: [' SCI ', ' Mary Lou Soleiman'].....
   """
   student_dict={}
   with open("C:\\Users\\hp\\Downloads\\students.txt", 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) >= 3:
                key = int(values[0])
                name = values[1]
                course = values[2]
                if key in student_dict:
                    student_dict[key][1].append(course)
                else:
                    student_dict[key] = [name, course]
   return student_dict

def sorting(studentList,enrollmentList,coursesList,ID):
   if validity(studentList,ID):
    studentCourses=enrollmentList[ID]
    print(studentCourses)
   else:
    print("Wrong ID")

def option1(enrollmentList,studentList,coursesList):
   studentID=int(input("Enter student ID: "))
   sorting(studentList,enrollmentList,coursesList,studentID)


def main():
   coursesList=courses()
   enrollmentList=enrollment()
   student_list=student_info()
   termination=True
   while termination:
      options()
      choice=int(input("Enter you choice :"))
      if choice==1:
         option1(enrollmentList,student_list,coursesList)
      elif choice==2:
         option2(coursesList,enrollmentList,student_list)
      elif choice==3:
         option3(enrollmentList,student_list,coursesList)
      elif choice==4:
         quit()
      else:
         print("Wrong choice ")
         break

if __name__=="__main__":
   main()
