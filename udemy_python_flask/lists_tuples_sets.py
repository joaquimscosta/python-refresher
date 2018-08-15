grades = [77, 80, 90]
tuple_grades = (77, 80, 90) # immutable
set_grades = {77, 80, 90} # unique & unordered

# print(sum(grades)/len(grades))
grades.append(108)
# print("grades = ", grades)
# print("grade[0] = ", grades[0])

tuple_grades = tuple_grades + (101,)
# print("tuple_grades = ", tuple_grades)

set_grades.add(123)
# print("set_grades = ", set_grades)

## Set operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

# print(your_lottery_numbers.intersection(winning_numbers))
# print(your_lottery_numbers.union(winning_numbers))
# print({1,2,3,4}.difference({1,2}))