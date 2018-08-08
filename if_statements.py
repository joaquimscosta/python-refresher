# should_continue = True
# if should_continue:
#     print("Hello")

# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person your know: ")

# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("you don't know {}".format(person))

## Exercise


def who_do_you_know():
    people = input("Who do you know (separated by comma)? ")
    return [person.strip() for person in people.split(",")]
    

def ask_user(people):
    person = input("Enter a name: ")
    if person in people:
        print("You know {}".format(person))
    else:
        print("You don't know {}".format(person))

ask_user(who_do_you_know())