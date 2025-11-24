import random

# --------------------------------------------
# Daily inspirational quotes
# --------------------------------------------
daily_quotes = [
    "You are stronger than you think.",
    "God is with you in every step you take.",
    "Even in the storm, you are not alone.",
    "Your purpose is bigger than your problems.",
    "You were created with strength and intention."
]

# --------------------------------------------
# Bible verses organized by emotion/struggle
# --------------------------------------------
verses = {
    "anxiety": [
        "Philippians 4:6-7 — Do not be anxious about anything...",
        "1 Peter 5:7 — Cast all your anxiety on Him because He cares for you."
    ],
    "sadness": [
        "Psalm 34:18 — The Lord is close to the brokenhearted...",
        "Revelation 21:4 — He will wipe every tear from their eyes."
    ],
    "stress": [
        "Matthew 11:28 — Come to me all who are weary and burdened...",
        "Psalm 55:22 — Cast your cares on the Lord and He will sustain you."
    ],
    "motivation": [
        "Joshua 1:9 — Be strong and courageous...",
        "Philippians 4:13 — I can do all things through Christ who strengthens me."
    ],
    "gratitude": [
        "1 Thessalonians 5:18 — Give thanks in all circumstances...",
        "Psalm 136:1 — Give thanks to the Lord, for He is good."
    ]
}

# --------------------------------------------
# Function: Show daily quote
# --------------------------------------------
def show_daily_quote():
    quote = random.choice(daily_quotes)
    print("\n✨ DAILY INSPIRATIONAL QUOTE ✨")
    print(quote)
    print()

# --------------------------------------------
# Function: Search verses by emotion
# --------------------------------------------
def search_verses():
    print("\nWhat are you feeling?")
    print("Options: anxiety, sadness, stress, motivation, gratitude")

    mood = input("Enter an emotion: ").lower()

    if mood in verses:
        print(f"\n📖 Bible verses for {mood.capitalize()}:")
        for v in verses[mood]:
            print(" - " + v)
    else:
        print("\nSorry, I don't have verses for that yet.")

# --------------------------------------------
# Main program loop
# --------------------------------------------
def main():
    print("=====================================")
    print("  🌟 DAILY INSPIRATION BIBLE APP 🌟")
    print("=====================================")

    show_daily_quote()

    while True:
        print("\nWhat would you like to do?")
        print("1. Search Bible verses by emotion")
        print("2. Get a new daily quote")
        print("3. Exit")

        choice = input("Enter a number (1-3): ")

        if choice == "1":
            search_verses()
        elif choice == "2":
            show_daily_quote()
        elif choice == "3":
            print("\nGoodbye! Stay blessed 🙏")
            break
        else:
            print("Invalid choice. Try again.")

# Run the app
main()
