class Course:
    def __init__(self,code='',name='',instructor=None):
        self.Code=code               #for the code of the course
        self.Name=name
        self.Instructor=instructor   #for the instructor(of Staff class) of the course
        self.StudentDict={}          #{student id:student object} for those students choosing the course 

    def setCode(self,code):
        self.Code=code

    def setName(self,name):
        self.Name=name

    def setInstructor(self,instructor):
        self.Instructor=instructor

    def addStudent(self,student):   #to add items corresponding to students selecting the course to the data field self.StudentDict
        '''
           To be fulfilled by the reader
        '''

    def __str__(self):
        return 'Course Code:'+self.Code
