***Author:Ben Chen from SSE in CUHKSZ, 2019/03/25, email:benchen@cuhk.edu.cn***

1.How to use the files in this folder(6-Course System):
	a. Run the file Course_Selection_System.py
	b. Enter '1' to indicate you are a student
	c. Enter your student id(The possible ids are stored in the file student.txt), for example:'118010001'
	d. Then you are allowed to select some courses you may want to take, enter the number before the code of the course to select it, you can choose several courses for one input, using comma ',' to seperate them. For example, enter '1,2,3,4,5'. 
	e. Then you are shown which courses you have chosen.
	f. Then press 'Enter' to end the selection process.
	g. Next user can use it to select courses.
	h. The same student can log in for the second time, if he adds more courses, then all courses including that he selected previously will be shown.
	i. After all students have chosen, the Adiministrator can log in by chosing '3', press 'Enter' and the whole program will end. And a file "CourseSelection.txt" will be created, which is a summary for the information of students selecting each courses.

2.The relationship structure of 5 classes(Person,Student,Staff,Course,System) defined: 
	a.Student and Staff are two subclasses of Person
	b.Student->select->Course, Staff->teach->Course
	c.System is a simulation of graphical interface of Course Selection System: 
	  System stores and allows updates for the information of all users(Student/Staff).

3.The principle of naming variables:
	a.For data fields, I always start with capital letters, like self.Name, self.StudentDict, etc.
	b.For methods, I always start with lowercase letters but with second words capitalized, like self.setName(), self.selectCourse(),etc
	c.For normal variables, I usually start with lowercase letter, for example, name, indexDict, etc.
	d.I quite often use dictionaries and lists in my program, and I always name them indicating what kind of elements are in them and end with 'Dict' or 'List', for example, studentDict, indexList etc. When I need one-to-one correspondance, I use dictionaries, and when I need order, I use lists.

4.Main data fields for each class:
	a.Person: self.Name(str) for the name of a person
	b.Student: self.Name inherited from Person class
		   self.ID(str) for the student id of a student and 
		   self.CourseDict {course code:course object} to store what courses does the student select, with key being course code and value being object from Course class
	c.Staff: self.Name(str) inherited from Person class
		 self.ID(str) for the staff id of a staff
		 self.Course for the course(of Course class) the staff teaches
	d.Course: self.Code(str) for the code of the course
		  self.Instructor for the instructor(of Staff class) of the course
		  self.StudentDict {student id:student object} for those students choosing the course 
	e.System: self.CourseDict {course code:course object} for all the courses provided for students to select
		  self.StudentDict {student id:student object} for all students 
		  self.StaffDict {staff id:staff object} for all staffs

5.Main methods for each class:
	a.For each class, I define setter for most data fields to avoid initializing using construtor, just to avoid confusion
	b.Student: def selectCourse(self,course) to add items corresponding to courses selected by students to the data field self.CourseDict
	c.Course: def addStudent(self,student) to add items corresponding to students selecting the course to the data field self.StudentDict
	d.System: def show(self) to simulate course selection process, showing the main menu for all courses 
		  def readStudentDict(self,file) to import information of all students from the student.txt file to the data fields self.StudentDict of System class
		  def readStaffDict(self,file) to import information of all staffs from the staff.txt file to the data fields self.StaffDict of System class
		  def generateFile(self) to generate a file storing all information after the selection process

6.This program is to be improved, partly the following points may be considered:
	a.Complete some data fields, like age, course name, students' major, students' score,password,lecture time and location etc.
	b.What staff can do is to be completed
	c.Define methods allowing students to check their course informaion, and their own timetable
	d.Allowing operations for dropping courses
	...