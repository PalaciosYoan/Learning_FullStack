def part3():
    user_word = input("Enter a word: ").lower()
    with open("PythonSummary.txt", "r") as f:
        content = f.read()
        content = content.lower()
        print(f"The word {user_word} occurs {content.count(user_word)} times")
        
part3()