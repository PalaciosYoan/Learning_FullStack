def addition():
    while True:
        try:
            user_input = input().split()
            # set_trace()
            for i in range(len(user_input)):
                user_input[i] = float(user_input[i])
            if len(user_input) == 1:
                print("Enter more than one int/float val...")
                continue
            print(sum(user_input))
            break
        except ValueError:
            print("A string was detected. try again ")
            
if __name__ == "__main__":
    addition()