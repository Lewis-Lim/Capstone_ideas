def calculate_gematria(word: str) -> int:
    """
    Calculates the standard Gematria value for a given Hebrew word.
    """
    # Mapping of Hebrew letters to their standard numerical values
    gematria_chart = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
        'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400,
        # Final letters (Sofit) - Standard gematria usually keeps their base values
        'ך': 20, 'ם': 40, 'ן': 50, 'ף': 80, 'ץ': 90
    }
    
    total_value = 0
    
    for letter in word:
        # Check if the character is a valid Hebrew letter in the chart
        if letter in gematria_chart:
            total_value += gematria_chart[letter]
            
    return total_value

# Test case 1: Ahava (אהבה) - meaning "Love"
ahava = "אהבה"
ahava_score = calculate_gematria(ahava)
print(f"The Gematria value for '{ahava}' (Ahava) is: {ahava_score}")

# Test case 2: Echad (אחד) - meaning "One"
echad = "אחד"
echad_score = calculate_gematria(echad)
print(f"The Gematria value for '{echad}' (Echad) is: {echad_score}")
