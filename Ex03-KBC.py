x = str(input("Enter your name: "))
print("Hello", x, ",", "Welcome to Kaun Banega Crorepati! \n")
print("rules of the game: \n1. You will be asked 5 questions, each with 4 options. \n2. You have to choose the correct option by entering the option number (1, 2, 3 or 4). \n3. If you choose the correct option, you will win the amount for that question and move on to the next question. \n4. If you choose the wrong option, you will lose and the game will end. \n5. You can quit the game at any time by entering 'q' or 'Q'. \n6. The amount won will be displayed at the end of the game. \n7. Good luck! \n")

Q1 = "Q1. According to Einstein's theory of relativity, as an object's speed approaches the speed of light, its mass:"
Q2 = "Q2. The dimensional formula for Planck's constant is the same as that of:"
Q3 = "Q3. According to Heisenberg's Uncertainty Principle, it is impossible to simultaneously determine with perfect accuracy:"
Q4 = "Q4. The First Law of Thermodynamics is essentially a statement of:"
Q5 = "Q5. According to Bohr's model of the hydrogen atom, the angular momentum of an electron in an orbit is quantized as:"

Op1 = "1. Decreases\n2. Remains constant\n3. Increases\n4. Becomes zero\n"
Op2 = "1. Energy\n2. Power\n3. Angular momentum\n4. Force\n"
Op3 = "1. Mass and volume of a particle\n2. Position and momentum of a particle\n3. Charge and mass of a particle\n4. Temperature and pressure of a gas\n"
Op4 = "1. Conservation of momentum\n2. Conservation of charge\n3. Conservation of energy\n4. Conservation of mass only\n"
Op5 = "1. mvr = nh\n2. mvr = nh/2π\n3. mvr = nh²\n4. mvr = 2πnh\n"

Ans = [3, 3, 2, 3, 2]  # correct answers for the questions
prizes = ["Rs. 1,000", "Rs. 10,000", "Rs. 1,00,000", "Rs. 10,00,000", "Rs. 1,00,00,000"]
questions = [Q1, Q2, Q3, Q4, Q5]
options = [Op1, Op2, Op3, Op4, Op5]

won_amount = "Rs. 0"

for i in range(5):
    print(questions[i])
    print(options[i])

    while True:
        ans = input("Enter your answer (1, 2, 3 or 4), or 'q' to quit: ")
        if ans.lower() == 'q':
            print(f"\nYou chose to quit the game. You leave with {won_amount}.")
            exit()
        if ans in ["1", "2", "3", "4"]:
            break
        print("Invalid input! Please enter a valid option number (1, 2, 3 or 4). \n")

    if ans == str(Ans[i]):
        won_amount = prizes[i]
        print(f"Correct answer! You have won {won_amount}. \n")
    else:
        print(f"Wrong answer! The correct answer is option {Ans[i]}.")
        print(f"Game over! You leave with {won_amount}.")
        exit()

print(f"\nCongratulations {x}! You answered all questions correctly and won {won_amount}!")
  