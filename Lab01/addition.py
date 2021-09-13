def addition():
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
            
if __name__ == "__main__":
    addition()