# SW 2 4th Quarter
from pyscript import display, document


class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        print(f"Hello! My name is {self.name}. I am from section {self.section}. My favorite subject is {self.favorite_subject}.")

# DISPLAY
print("\n=== Classmate Introductions ===\n")
for cm in classmates:
    cm.introduce()

# ADD
print("\n=== Add a New Classmate ===")
try:
    name = input("Enter name: ")
    section = input("Enter section: ")
    favorite_subject = input("Enter favorite subject: ")

    new_classmate = Classmate(name, section, favorite_subject)
    classmates.append(new_classmate)

    print("\n=== Updated Classmate List ===\n")
    for cm in classmates:
        cm.introduce()

except:
    print("Something went wrong with the input. Please try again.")