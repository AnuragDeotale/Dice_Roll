import random

while True:
    x = input("Do you want to roll the dice? (Y/N): ").strip().lower()
    
    if x == "y":
        no = random.randint(1, 6)
        
        if no == 1:
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
        elif no == 2:
            print("[0    ]")
            print("[     ]")
            print("[    0]")
        elif no == 3:
            print("[0    ]")
            print("[  0  ]")
            print("[    0]")
        elif no == 4:
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
        elif no == 5:
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
        elif no == 6:
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
        print("\n")
    elif x == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter 'Y' or 'N'.\n")
