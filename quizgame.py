import random

# -----------------------------
# CODEQUEST - THE HACKER'S TRIAL
# -----------------------------

print("=" * 45)
print("          CODEQUEST 🔐")
print("       THE HACKER'S TRIAL")
print("=" * 45)

print("\nWelcome, Hacker!")
print("Your mission is to answer the challenges")
print("and unlock the mysterious digital vault.")
print("\nYou have 3 lives.")
print("Each correct answer gives you 10 points.")
print("Let's begin!\n")

# Questions
questions = [
    {
        "question": "Which language is mainly used to structure a webpage?",
        "options": ["A) Python", "B) HTML", "C) Java", "D) C++"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used to start a comment in Python?",
        "options": ["A) //", "B) /*", "C) #", "D) <!--"],
        "answer": "C"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["A) String", "B) Integer", "C) Boolean", "D) Float"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) function", "B) def", "C) func", "D) define"],
        "answer": "B"
    },
    {
        "question": "Which of these is NOT a programming language?",
        "options": ["A) Python", "B) Java", "C) HTML", "D) C++"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A) Central Processing Unit",
            "B) Computer Processing Utility",
            "C) Central Program Unit",
            "D) Control Processing Unit"
        ],
        "answer": "A"
    },
    {
        "question": "Which loop is commonly used to repeat through a list in Python?",
        "options": ["A) for", "B) repeat", "C) loop", "D) iterate"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for equality comparison in Python?",
        "options": ["A) =", "B) ==", "C) !=", "D) ==="],
        "answer": "B"
    },
    {
        "question": "Which technology is commonly used to style webpages?",
        "options": ["A) HTML", "B) CSS", "C) SQL", "D) Python"],
        "answer": "B"
    },
    {
        "question": "Which data structure stores key-value pairs in Python?",
        "options": ["A) List", "B) Tuple", "C) Dictionary", "D) Set"],
        "answer": "C"
    }
]

# Hints for each question
hints = [
    "Think about the language that uses tags such as <body> and <h1>.",
    "Python uses a single symbol to write comments.",
    "It represents only two possible values.",
    "Python functions begin with a special three-letter keyword.",
    "One of these is a markup language rather than a programming language.",
    "Think about the main component that processes instructions.",
    "This loop is commonly used when going through items one by one.",
    "One equal sign assigns a value. The other compares values.",
    "Think about colors, fonts and page appearance.",
    "This structure connects a key to its corresponding value."
]

# Shuffle questions so the game is different each time
random.shuffle(questions)

score = 0
lives = 3
correct_answers = 0

# -----------------------------
# GAME LOOP
# -----------------------------

for number, question in enumerate(questions, start=1):

    if lives == 0:
        break

    print("\n" + "-" * 45)
    print(f"⚡ CHALLENGE {number}")
    print("-" * 45)

    print(question["question"])

    for option in question["options"]:
        print(option)

    print("\n💡 Type H for a hint.")
    user_answer = input("Your answer: ").strip().upper()

    # Hint system
    if user_answer == "H":
        print("\n💡 HINT:")
        
        # Find the hint using the question index
        original_index = questions.index(question)
        print(hints[original_index])

        user_answer = input("\nYour answer: ").strip().upper()

    # Check answer
    if user_answer == question["answer"]:
        score += 10
        correct_answers += 1

        print("\n✅ ACCESS GRANTED!")
        print("+10 points")
        print(f"⭐ Current Score: {score}")

        # Special messages based on score
        if score >= 80:
            print("🔥 Excellent! You are becoming a Code Master!")

        elif score >= 50:
            print("⚡ Nice work! The system is impressed.")

        else:
            print("🔓 Security layer breached!")

    else:
        lives -= 1

        print("\n❌ ACCESS DENIED!")
        print("That answer is incorrect.")
        print(f"💔 Lives remaining: {lives}")

        if lives > 0:
            print("Don't give up! The next challenge is waiting.")

# -----------------------------
# FINAL RESULT
# -----------------------------

print("\n" + "=" * 45)
print("             GAME OVER")
print("=" * 45)

print(f"\n⭐ Final Score: {score}/100")
print(f"✅ Correct Answers: {correct_answers}/10")
print(f"💔 Lives Remaining: {lives}")

# Final result based on score
if score >= 80:
    print("\n🏆 VAULT UNLOCKED!")
    print("Rank: CODE MASTER 👑")
    print("The system recognizes your skills.")
    print("MISSION COMPLETE! 🚀")

elif score >= 50:
    print("\n🔓 PARTIAL ACCESS GRANTED!")
    print("Rank: SKILLED HACKER ⚡")
    print("You are close to unlocking the vault!")

else:
    print("\n🔒 VAULT REMAINS LOCKED!")
    print("Rank: ROOKIE HACKER 🥷")
    print("Keep practicing and try again!")

print("\nThank you for playing CODEQUEST! 🎮")
print("=" * 45)