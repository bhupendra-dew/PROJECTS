# Python code to play 21 Number Game returns the nearest multiple to 4

def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\nYOU LOSE!!!")
    print("Better luck next time.")
    exit(0)

# Checking wheter the number are consecutive
    
def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
        i = i + 1
    return True

# Main function to play the game

def start1():
    xyz = []
    last = 0
    while True:
        
        print("Enter 'F' to take first chance.")
        print("Enter 'S' to take second chance.")
        print("Enter 'Q' to quit the game.")
        
        chance = input("Enter your choice: ")

        if chance == 'F':
            while True:
                if last == 20:
                    lose1()
                else:
                    print("\nYour Turn.")
                    print("How many numbers do you wish to enter?")
                    inp = int(input("Enter your choice: "))

                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqualified.") 
                        lose1()

                    i, j = 1, 1

                    print("Now enter the values.")
                    while i <= inp:
                        a = input("Enter the number: ")
                        a = int(a)
                        xyz.append(a)
                        i += 1

                    # Storing the last number entered by the user in xyz
                        
                    last = xyz[-1]

                    # Checking whether the numbers entered by the user are consecutive or not

                    if check(xyz) == True:
                        if last == 21:
                            lose1()
                        else:
                            while j <= comp:
                                last = last + 1
                                xyz.append(last)
                                j += 1
                            print("Order of inputs after computer's turn: ", xyz)
                            last = xyz[-1]
                    else:
                        print("\n You did not input consecutive numbers.")
                        lose1()

        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                # Computer's Turn
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j = j + 1
                print("Order of inputs after computer's turn: is:", xyz)

                if xyz[-1] == 20:
                    lose1()

                else:
                    print("\nYour Turn.")
                    print("How many numbers do you wish to enter?")
                    inp = int(input("Enter your choice: "))
                    inp = int(inp)
                    i = 1
                    print("Now enter the values.")
                    
                    while i <= inp:
                        xyz.append(int(input("Enter the number: ")))
                        i = i + 1
                    last = xyz[-1]
                    if check(xyz) == True:
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        print("\nYou did not input consecutive numbers.")
                        lose1()
            print("\n\nCongratulations!!!")
            print("You win the game.")
            exit(0)
        
        else:
            print("Wrong choice.")

# Driver code
game = True
while game == True:
    print("Play 21 Number Game.")
    print("Player 2 is Computer.")
    print("Do you want to play the game?")
    ans = input("Enter your choice: ")
    if ans == "yes" or "Yes":
        start1()
    else:
        print("Thank you for playing the game.")
        game = False
        exit(0)

                