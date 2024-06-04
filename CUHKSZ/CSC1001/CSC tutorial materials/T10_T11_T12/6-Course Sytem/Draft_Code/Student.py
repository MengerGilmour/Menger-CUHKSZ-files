from Person import Person

class Student(Person):
    def __init__(self,ID='',major=''):     #A tip:Do not initialize a dictionary using default value {}, the dictionary may be the same if you create another object
        super().__init__()
        self.ID=ID              #for the student id of a student
        self.Major=major
        self.CourseDict={}      #{course code:course object} to store what courses does the student select, with key being course code and value being object from Course class

    def setID(self,ID):
        self.ID=ID

    def setMajor(self,major):
        self.Major=major

    #to add items corresponding to courses selected by students to the data field self.CourseDict
    def selectCourse(self,course):
        '''
           To be fulfilled by the reader
        '''

    def dropCourse(self,course):
        self.CourseDict.pop(course.Code)

    def __str__(self):
        return "ID:"+self.ID+'\t\tName:'+self.Name


