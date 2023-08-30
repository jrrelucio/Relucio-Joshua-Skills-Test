class Account:

    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

class StudentAccount(Account):

    def __init__(self, ID, name, classes=None, is_enlistment_locked=None, is_enlisted=None):
        super().__init__(ID, name)
        self.is_enlistment_locked = is_enlistment_locked
        self.is_enlisted = is_enlisted

        if classes is None:
            self.classes = []
        else:
            self.classes = classes

        if is_enlistment_locked is None:
            self.is_enlistment_locked = False
        else:
            self.is_enlistment_locked = is_enlistment_locked

        if is_enlisted is None:
            self.is_enlisted = False
        else:
            self.is_enlisted = is_enlisted
    
    def add_class(self, cls):
        if cls not in self.classes:
            self.classes.append(cls)
    
    def lock_enlistment(self):
        if self.is_enlistment_locked == False:
            self.is_enlistment_locked = True
            print(self.name + " has locked enlistment.")  
        else:
            print("Error: " + self.name + "has already locked their enlistment.")  

class AdviserAccount(Account):

    def __init__(self, ID, name, enlisted_advisees=None, advisees=None):
        super().__init__(ID, name)
        self.enlisted_advisees = enlisted_advisees
        if advisees is None:
            self.advisees = []
        else:
            self.advisees = advisees

        if enlisted_advisees is None:
            self.enlisted_advisees = []
        else:
            self.enlisted_advisees = enlisted_advisees

    def add_advisee(self, adv):
        if adv not in self.advisees:
            self.advisees.append(adv)
            print(self.name + " has added " + adv.name + " as an advisee.")
        else: #extra case: if adviser already has advisee on their list.
            print("Error: " + self.name + "has already added" + adv.name + "as an advisee.")
    
    def print_advisees(self):
        for adv in self.add_advisee:
            print(adv)
    
    def lock_enlistment_for(self, adv):
        if adv not in self.advisees:
            print("Error: " + adv.name + " is not an advisee of " + self.name)
        elif adv.is_enlistment_locked == False:
            print("Error: " + adv.name + "\'s enlistment is not locked yet.")
        elif adv.is_enlisted: #extra case: if adviser attempts to enlist an already enlisted student
            print("Error: " + adv.name + " has already been enlisted")
        else:
            adv.is_enlisted = True
            print(adv.name + " is now enlisted.")

#Testing

student1 = StudentAccount("05524", "Ross")
student1.add_class("Class 1")
student1.add_class("Class 2")
student1.add_class("Class 4")
student1.lock_enlistment()

adviser = AdviserAccount("01341", "Rachel")
adviser.add_advisee(student1)
adviser.lock_enlistment_for(student1)

student2 = StudentAccount("12345", "Chandler")
student2.add_class("Class 1")
student2.add_class("Class 3")

adviser.add_advisee(student2)
adviser.lock_enlistment_for(student2)

student3 = StudentAccount("01353", "Joey")
student3.add_class("Class 5")
student3.add_class("Class 9")

adviser.lock_enlistment_for(student3)