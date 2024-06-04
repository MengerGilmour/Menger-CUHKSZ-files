from Student import Student
from Staff import Staff
from Course import Course

#System class is a simulation of graphical interface of Course Selection System: 
#System class stores and allows updates for the information of all users(Student/Staff).
class System:
    def __init__(self):
        self.CourseDict={} #{course code:course object} for all the courses provided for students to select
        self.StudentDict={} #{student id:student object} for all students 
        self.StaffDict={}   #{staff id:staff object} for all staffs
        
    #def show(self) to simulate course selection process, showing the main menu for all courses     
    def show(self):
        '''
           To be fulfilled by the reader
        '''
                    
            
    #def readStudentDict(self,file) to import information of all students from the student.txt file to the data fields self.StudentDict of System class           
    def readStudentDict(self,file):
        '''
           To be fulfilled by the reader
        '''
        
    #def readStaffDict(self,file) to import information of all staffs from the staff.txt file to the data fields self.StaffDict of System class
    def readStaffDict(self,file):
        '''
           To be fulfilled by the reader
        '''

    #def generateFile(self) to generate a file storing all information after the selection process       
    def generateFile(self):
        '''
           To be fulfilled by the reader
        '''


