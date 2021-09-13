import json
from pdb import set_trace
def part1():
    while True:
        try:
            user_input = input().split()
            # set_trace()
            for i in range(len(user_input)):
                user_input[i] = float(user_input[i])
            print(sum(user_input))
            break
        except ValueError:
            print("Not enough values inputted or a string was detected. try again ")

def part2():
    user_sentence = input("Enter a sentence: ")
   
    while True:
        try:
            repeated = int(input("How many times should I repeat the setence? "))
            break
        except ValueError:
            print("error: ENTER A INT!")
    with open("CompletedPunishment.txt" , "w") as f:
        for i in range(repeated):
            f.write(user_sentence + '\n')


def part3():
    user_word = input("Enter a word: ").lower()
    with open("PythonSummary.txt", "r") as f:
        content = f.read()
        content = content.lower()
        print(f"The word {user_word} occurs {content.count(user_word)} times")

class ClassSchedule:
    def __init__(self, department, 
                number, name, credits, 
                lecture_days, start_time, end_time, avg_grade):
        self.department = department
        self.number = number
        self.name = name
        self.credits = credits
        self.lecture_days = lecture_days
        self.start = start_time
        self.end = end_time
        self.avg_grade = avg_grade


def part4():
    """ This has to be part of the classs"""
    out = [] #storing object for each class
    with open("classesInput.txt", "r") as f:
        count = 9
        class_info = []
        lines = f.readlines()
        for line in lines:
            if count == 0:
                count = 8
                obj = ClassSchedule(class_info[0], class_info[1],
                                    class_info[2], class_info[3],
                                    class_info[4], class_info[5],
                                    class_info[6], class_info[7])
                out.append(obj)
            if count == 9:
                count -= 1
                continue
            line = line.replace("\n","")
            class_info.append(line)
            count -= 1
    count = 1
    with open("classesOutput.txt", "w") as f:
        for c in out:
            f.write(f"COURSE {count}: {c.department}{c.number}: {c.name}\n")
            f.write(f"Number of Credits: {c.credits}\n")
            f.write(f"Days of Lectures: {c.lecture_days}\n")
            f.write(f"Lecture Time: {c.start} - {c.end}\n")
            f.write(f"Stat: on average, students get {c.avg_grade} in this course\n\n")
            count += 1

def part5():
    with open("grades.txt", "w+") as f:
        content = f.read()
        grades_dict = json.loads(content)
        
        while True:
            todo = input("What would you like to do? (create student: a, request grade: b, edit grade: c, delete grade: d) ")
            if todo == "a":
                name = input("Enter name of new Student: ")
                grade = input(f"Enter grade of {name}: ")
                grades_dict[name] = grade
                # set_trace()
                
            elif todo == "b":
                while True:
                    name = input("Enter name of student to get you the grade: ")
                    if name in grades_dict:
                        print(f"{name}'s grade is {grades_dict[name]}")
                        break
                    else:
                        print("That student doesn't exist.. try again")
            elif todo == "c":
                while True:
                    name = input("What student would you like to edit today? ")
                    if name not in grades_dict:
                        print("Student doesn't exit. Try again...")
                        continue
                    
                    grade = input("What grade would you like to give them? ")
                    grades_dict[name] = float(grade)
                    
                    break
                
            elif todo == "d":
                while True:
                    name = input("For what student you would like to delete grade for? ")
                    if name in grades_dict:
                        grades_dict[name] = None
                        
                        break
                    else:
                        print("Try again... Student doesn't exist")
                
            else:
                print("Enter a valid input...")
                continue

            again = input("Would u like to do something else? (y/n)").lower()
            if again != "y":
                break
        json.dump(grades_dict, f)
    
    
def main():
    #part1()
    #part2()
    #part3()
    #part4()
    part5()
    



if __name__ == "__main__":
    main()