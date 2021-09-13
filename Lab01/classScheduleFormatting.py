class ClassSchedule:
    def __init__(self, department=None, 
                number=None, name=None, credits=None, 
                lecture_days=None, start_time=None, end_time=None, avg_grade=None):
        self.department = department
        self.number = number
        self.name = name
        self.credits = credits
        self.lecture_days = lecture_days
        self.start = start_time
        self.end = end_time
        self.avg_grade = avg_grade
        self.out = []


    def extractContent(self):
        """ This has to be part of the classs"""
        with open("classesInput.txt", "r") as f:
            count = 9
            class_info = []
            lines = f.readlines()
            
            for line in lines:
                line = line.replace("\n","")
                print(line, count)
                if count == 0:
                    count = 8
                    obj = ClassSchedule(class_info[0], class_info[1],
                                        class_info[2], class_info[3],
                                        class_info[4], class_info[5],
                                        class_info[6], class_info[7])
                    self.out.append(obj)
                    class_info = []
                if count == 9:
                    count -= 1
                    continue
                
                class_info.append(line)
                count -= 1
            #Creating the final object for the final classs
            obj = ClassSchedule(class_info[0], class_info[1],
                                        class_info[2], class_info[3],
                                        class_info[4], class_info[5],
                                        class_info[6], class_info[7])
            self.out.append(obj)
            
            
    def outputContent(self):
        count = 1
        with open("classesOutput.txt", "w") as f:
            for c in self.out:
                f.write(f"COURSE {count}: {c.department}{c.number}: {c.name}\n")
                f.write(f"Number of Credits: {c.credits}\n")
                f.write(f"Days of Lectures: {c.lecture_days}\n")
                f.write(f"Lecture Time: {c.start} - {c.end}\n")
                f.write(f"Stat: on average, students get {c.avg_grade} in this course\n\n")
                count += 1

run = ClassSchedule()
run.extractContent()
run.outputContent()