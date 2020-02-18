class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects
    
    def testAVG(self,score1, score2, score3):
        avg=(score1+score2+score3)/3
        return avg

Mo = Student("Mo",24,["Maths","Physics","Chemistry"])
print(Mo.subjects)
print(Mo.testAVG(72,68,92))