class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_one.numbers = (1, 2, 3, 6, 7, 8)
player_two = LotteryPlayer("John")

# print(player_one.name)
# print(player_one.numbers)
# print(player_one.total())
# print(player_one.name==player_two.name)


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        if len(self.marks) == 0:
            return 0
        else:
            return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to school.")


anna = Student("Anna", "MIT")
anna.marks.append(56)
print(anna.marks)
print(anna.average())
Student.go_to_school()