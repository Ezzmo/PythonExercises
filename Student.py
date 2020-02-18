class Student:
    def __init__(self, name, age, mscore, sscore, escore):
        self.name = name
        self.age = age
        self.mscore = mscore
        self.sscore = sscore
        self.escore = escore
    
    def testAVG(self):
        try:
            avg=(self.mscore+self.sscore+self.escore)/3
            return avg
        except:
            print("Invalid score values,")

Mo = Student("Mo",24,28,28,32)

print(Mo.testAVG())
