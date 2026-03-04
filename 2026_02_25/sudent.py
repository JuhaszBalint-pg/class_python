class Student:

    #constructor
    def __init__(self, name, age, height, gender, score):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        self.score = score

    def learn(self, test):
        self.score += test

    def __str__(self):
        return(f'Hello! I am {self.name}, {self.age} age, {self.height} tall, sex : {self.gender}, {self.score} scorecard')
    
    def introduce(self):
        return f'Hello, my name is {self.name}, i am {self.age} old'

Lajos = Student('Lajos', 13, 178, 'Megatron', 0)

print(Lajos)

Anna = Student('Anna', 15, 170, 'Female', 100)

print(Anna)

Lajos.learn(100)

print(Lajos.score)
print(Lajos.introduce())