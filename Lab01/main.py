
def part1():
    while True:
        try:
            user_input = input().split()
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
    pass

def main():
    part3()
    



if __name__ == "__main__":
    main()