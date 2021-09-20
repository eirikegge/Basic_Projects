#!/usr/bin/env python
# coding: utf-8

# In[119]:


class Student():
    def __init__(self, first_name, last_name, dob, email, Id, courses = None, grades = None):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.Id = Id
        
        #courses
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
            
        #grades
        if grades is None: 
            self.grades = {}
        else: 
            self.grades = grades

    def assign_grade(self, course, grade):
        if grade <= 6 or grade >= 0: 
            self.grades[course.name] = grade #adds grade to student 
            course.all_grades[str(self.Id)] = grade #adds student id and grade to course (obj. get gpa for course)
        else: 
            raise Exception('Invalid Grade')
        
    def get_gpa(self):
        gpa = sum(self.grades.values()) / len(self.courses)
        return round(gpa, 2)
        

    def __repr__(self):
        structure = "Person(First Name:'{0}', Last Name:'{1}', Date of Birth:'{2}', Email:'{3}', ID:'{4}', Enrolled in:'{5}', Grades:'{6}', GPA: '{7}')"
        return structure.format(self.first_name, self.last_name, self.dob, self.email, self.Id, self.courses, self.grades, self.get_gpa())
    
    
    
class Course():
    def __init__(self, name, max_students, all_grades = None):
        self.name = name
        self.max_students = max_students
        self.students = []
        
        #grade dict with student Id
        if all_grades is None: 
            self.all_grades = {}
        else:
            self.all_grades = all_grades
        
    def add_student(self, student):
        if len(self.students) < self.max_students and self.name not in student.courses: 
            self.students.append(student.Id) #adds student id to course (proof of enrollment)
            student.courses.append(self.name) #adds course to student info list (to see which courses he/she has)
        else:
            raise Exception('Course is full')
            
    def get_course_gpa(self):
        course_gpa = sum(self.all_grades.values()) / len(self.students)
        return round(course_gpa, 2)
        
    def __repr__(self):
        structure = "Course(Course Name: '{0}', Enrolled Students: '{1}', Free Cap.: '{2}', Max. Cap.: '{3}', Grades: '{4}', Course GPA: '{5}')"
        return structure.format(self.name, self.students, (self.max_students - len(self.students)),  self.max_students, self.all_grades, self.get_course_gpa())
    


# In[120]:


#define students 
s1 = Student('John', 'Jacobsen', '05/07/1997', 'john.jacobsen@icloud.com', 12341234)
s2 = Student('Olav', 'Mathiasen', '30/11/1996', 'olav.mathiasen@gmail.com', 12341233)
s3 = Student('Mats', 'Jacobsen', '01/01/2001', 'mats.jacobsen@hotmail.com', 12341232)
s4 = Student('Ola', 'Petterson', '05/06/1985', 'ola.petterson@live.com', 12341231)
s5 = Student('Axel', 'Hennie', '05/06/1985', 'axel.hennie@live.com', 12341231)

#define courses
c1 = Course('Physics', 5)
c2 = Course('Chemistry', 5)
c3 = Course('Math', 5)
c4 = Course('Biology', 5)

#list of students & courses 
students = [s1, s2, s3, s4, s5]
courses = [c1, c2, c3, c4]

#assign courses to students
for i in students:
    c1.add_student(i)
    
for i in students:
    c2.add_student(i)

c3.add_student(s1)
c3.add_student(s2)
c3.add_student(s3)

c4.add_student(s1)
c4.add_student(s5)


#assign grade to all students
s1.assign_grade(c1, 6)
s2.assign_grade(c1, 5)
s3.assign_grade(c1, 4)
s4.assign_grade(c1, 3)
s5.assign_grade(c1, 5)

s1.assign_grade(c2, 3)
s2.assign_grade(c2, 4)
s3.assign_grade(c2, 6)
s4.assign_grade(c2, 6)
s5.assign_grade(c2, 2)

s1.assign_grade(c3, 5)
s2.assign_grade(c3, 2)
s3.assign_grade(c3, 1)

s1.assign_grade(c4, 6)
s5.assign_grade(c4, 1)


#get gpa for a student
print(s1.get_gpa())
print(s2.get_gpa())
print(s3.get_gpa())
print(s4.get_gpa())
print(s5.get_gpa())

#get student info
for i in students:
    print(i)

#get course info
for i in courses: 
    print(i)


# #TBD:
# * Raise Exceptions for assigning grade to students not enrolled in program
