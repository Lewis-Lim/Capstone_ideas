TOPICS = {
    "1": (
        "Advice on not knowing what to do:\n"
        " - Step back: Overthinking breeds paralysis.\n"
        " - Pick the smallest action: Take a step that takes under 2 minutes.\n"
        " - Focus on process over outcome: Prioritize momentum over perfection."
    ),
    "2": (
        "Advice on removing superstition:\n"
        " - Examine the logic: Trace the real cause-and-effect chain.\n"
        " - Track occurrences: Keep a log to test if the rule actually holds true.\n"
        " - Test small exposures: Break a minor habit and observe that nothing bad happens."
    )
}

def main():
    print("=" * 40)
    print("      DAILY STARTUP ASSISTANT      ")
    print("=" * 40)
    print("\nSelect a topic:")
    print("1. Advice on not knowing what to do")
    print("2. Advice on removing superstition")
    
    choice = input("\nEnter choice number (1 or 2): ").strip()
    
    print("\n" + "-" * 40)
    if choice in TOPICS:
        print(TOPICS[choice])
    else:
        print("Invalid selection. Reload the page to try again.")
    print("-" * 40)

if __name__ == "__main__":
    main()