from Person import Person

class Staff(Person):
    def __init__(self,ID='',course=None):
        super().__init__()
        self.ID=ID             #for the staff id of a staff
        self.Course=course     #for the course(of Course class) the staff teaches

    def setID(self,ID):
        self.ID=ID

    def setCourse(self,course):
        self.Course=course
