import unicodedata

def get_hebrew_gematria(text):
    hebrew_values = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50,
        'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100, 'ר': 200,
        'ש': 300, 'ת': 400
    }
    return sum(hebrew_values.get(char, 0) for char in text)

def get_greek_isopsephy(text):
    greek_values = {
        'α': 1, 'ά': 1, 'ὰ': 1, 'ᾶ': 1, 'ἀ': 1, 'ἁ': 1, 'ἄ': 1, 'ἅ': 1, 'ἆ': 1, 'ἇ': 1,
        'β': 2, 'γ': 3, 'δ': 4, 'ε': 5, 'έ': 5, 'ὲ': 5, 'ἐ': 5, 'ἑ': 5, 'ἔ': 5, 'ἕ': 5,
        'ϝ': 6, 'ϛ': 6,
        'ζ': 7, 'η': 8, 'ή': 8, 'ὴ': 8, 'ῆ': 8, 'ἠ': 8, 'ἡ': 8, 'ἤ': 8, 'ἥ': 8, 'ἦ': 8, 'ἧ': 8,
        'θ': 9, 'ι': 10, 'ί': 10, 'ὶ': 10, 'ῖ': 10, 'ἰ': 10, 'ἱ': 10, 'ἴ': 10, 'ἵ': 10, 'ἶ': 10, 'ἷ': 10,
        'κ': 20, 'λ': 30, 'μ': 40, 'ν': 50, 'ξ': 60, 'ο': 70, 'ό': 70, 'ὸ': 70, 'ὀ': 70, 'ὁ': 70, 'ὄ': 70, 'ὅ': 70,
        'π': 80, 'ϙ': 90, 'ϟ': 90,
        'ρ': 100, 'ῥ': 100, 'σ': 200, 'ς': 200, 'τ': 300,
        'υ': 400, 'ύ': 400, 'ὺ': 400, 'ῦ': 400, 'ὐ': 400, 'ὑ': 400, 'ὔ': 400, 'ὕ': 400, 'ὖ': 400, 'ὗ': 400,
        'φ': 500, 'χ': 600, 'ψ': 700, 'ω': 800, 'ώ': 800, 'ὼ': 800, 'ῶ': 800, 'ὠ': 800, 'ὡ': 800, 'ὤ': 800, 'ὥ': 800, 'ὦ': 800, 'ὧ': 800,
        'ϡ': 900
    }
    
    # Lowercase the entire string to seamlessly handle capital Greek letters (e.g., Ιησοῦς -> ιησοῦς)
    normalized_text = text.lower()
    return sum(greek_values.get(char, 0) for char in normalized_text)


def main():
    while True:
        print("\n--- GEMATRIA & ISOPSEPHY CALCULATOR ---")
        print("1. Hebrew Gematria")
        print("2. Greek Isopsephy")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ").strip()

        if choice == '1':
            user_text = input("Enter Hebrew text: ").strip()
            val = get_hebrew_gematria(user_text)
            print(f"Result for '{user_text}': {val}")
        elif choice == '2':
            user_text = input("Enter Greek text (uppercase or lowercase): ").strip()
            val = get_greek_isopsephy(user_text)
            print(f"Result for '{user_text}': {val}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()