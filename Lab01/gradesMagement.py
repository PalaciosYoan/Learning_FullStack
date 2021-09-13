import json
def part5():
    with open("grades.txt", "r+") as f:
        content = f.read()
        grades_dict = json.loads(content)
        f.seek(0)
        f.truncate()
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
            
            print(grades_dict)
            again = input("Would u like to do something else? (y/n)").lower()
            if again != "y":
                break
    
        json.dump(grades_dict, f)
part5()