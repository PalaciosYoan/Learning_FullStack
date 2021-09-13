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
            
part2()