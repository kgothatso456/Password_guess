import random

COLORS= ["P", "B", "G", "O", "Y", "W"]
ATTEMPTS= 10
CODE_LENGTH= 4

def generate_code():
    code=[]

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"YOu must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break
            
    return guess

def check_code(guess, real_code):
    color_count={}
    correct_position= 0
    incorrect_position=0

    for color in real_code:
        if color not in color_count:
            color_count[color]=0
        color_count[color]+=1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_position+=1
            color_count[guess_color]-=1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_count and color_count[guess_color]>0:
            incorrect_position += 1
            color_count[guess_color] -=1

    return correct_position, incorrect_position

def game():
    print(f"Welcome to password, you have {ATTEMPTS} to guess the code....")
    print("The valid colors are", *COLORS)
    
    code = generate_code()
    for attempt in range(1, ATTEMPTS + 1):
        guess = guess_code()
        correct_position, incorrect_position = check_code(guess, code)
        
        if correct_position == CODE_LENGTH:
            print(f"You guessed the code in {attempt} tries!")
            break

        print(f"Correct positions: {correct_position} | Incorrect position {incorrect_position}")

    else:
        print(f"You ran out of tries, the code was:", *code)

if __name__ == "__main__":
    game()