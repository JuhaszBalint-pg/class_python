class Student:
    name = ''
    age = 0
    height = 0
    gender = ''
    score = 0

    def learn(self, test):
        self.score += test

    def __str__(self):
        return(f'Hello! I am {self.name}, {self.age} age, {self.height} tall, sex : {self.gender}, {self.score} scorecard')

Lajos = Student()
Lajos.name = 'Lajos'
Lajos.age = 13
Lajos.height = 178
Lajos.gender = 'Megatron'
Lajos.score = 1

Anna = Student()

print(Lajos)
print(Anna)