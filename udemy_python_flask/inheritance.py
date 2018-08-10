class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    
    @classmethod
    def friend(cls, origin, name, *args, **kwargs):
        return cls(name, origin.school, *args, **kwargs)

# 
class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

anna = WorkingStudent('Anna', 'MIT', 123.00, 'Software Engineer')
john = WorkingStudent.friend(anna, 'John', 17.23, job_title='Software Engineer')
print(anna.salary)

print(john.name)
print(john.school)
print(john.salary)
print(john.job_title)

