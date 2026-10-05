import unicodedata


def get_greek_isopsephy(text):
    """
    Calculates the Isopsephy (gematria) value of Koine Greek text.
    Decomposes Greek diacritics automatically and calculates totals.
    """
    greek_values = {
        'α': 1, 'β': 2, 'γ': 3, 'δ': 4, 'ε': 5, 'ϛ': 6, 'ϝ': 6,
        'ζ': 7, 'η': 8, 'θ': 9, 'ι': 10, 'κ': 20, 'λ': 30, 'μ': 40,
        'ν': 50, 'ξ': 60, 'ο': 70, 'π': 80, 'ϙ': 90, 'ϟ': 90,
        'ρ': 100, 'σ': 200, 'ς': 200, 'τ': 300, 'υ': 400, 'φ': 500,
        'χ': 600, 'ψ': 700, 'ω': 800, 'ϡ': 900
    }

    normalized = unicodedata.normalize('NFD', text.lower())
    base_greek = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
    return sum(greek_values.get(char, 0) for char in base_greek)


# Structured by Cognitive Clusters (Chunking & Contrastive Pedagogy)
pedagogical_database = [
    {
        "category": "1. THE COGNITIVE PAIR (888 vs 666)",
        "items": [
            {
                "greek": "Ἰησοῦς",
                "transliteration": "Iēsous (Jesus)",
                "verse": "Matthew 1:21",
                "value": 888,
                "mnemonic": "TRIPLE 8: 8 is the Day of Resurrection (new week). Jesus = 888 (Resurrection in full completeness)."
            },
            {
                "greek": "χξϛ",
                "transliteration": "Chi Xi Stigma (666)",
                "verse": "Revelation 13:18",
                "value": 666,
                "mnemonic": "TRIPLE 6: 6 is human imperfection (created on Day 6). 666 = Man attempting to mimic God."
            }
        ]
    },
    {
        "category": "2. THE PERFECT EQUIVALENCE (801 = Alpha/Omega & Dove)",
        "items": [
            {
                "greek": "Ἀλφα καὶ Ὦ",
                "transliteration": "Alpha kai O (Alpha and Omega)",
                "verse": "Revelation 1:8",
                "value": 801,
                "mnemonic": "Beginning (1) + End (800) = 801. Represents Jesus as the Eternal Source."
            },
            {
                "greek": "περιστερά",
                "transliteration": "Peristera (Dove)",
                "verse": "Matthew 3:16",
                "value": 801,
                "mnemonic": "DOVE = 801. The Spirit (Dove) at baptism matches the Eternal Alpha & Omega (801)."
            }
        ]
    },
    {
        "category": "3. THE SACRED FACTOR 37 (Jesus Christ & Truth)",
        "items": [
            {
                "greek": "Ἰησοῦς Χριστός",
                "transliteration": "Iēsous Christos (Jesus Christ)",
                "verse": "John 1:17",
                "value": 2368,
                "mnemonic": "2368 = 37 x 64. Notice that 37 is the foundational prime factor!"
            },
            {
                "greek": "ἀλήθεια",
                "transliteration": "Aletheia (Truth)",
                "verse": "John 14:6",
                "value": 64,
                "mnemonic": "TRUTH = 64. Therefore, Jesus Christ (2368) = 37 x TRUTH (64)."
            }
        ]
    },
    {
        "category": "4. SHORT BENCHMARK NUMBERS (Double Digits)",
        "items": [
            {
                "greek": "Ἀγάπη",
                "transliteration": "Agape (Love)",
                "verse": "1 Corinthians 13:13",
                "value": 93,
                "mnemonic": "93 = Unconditional Divine Love. (Visual anchor: '93 Love Lane')."
            },
            {
                "greek": "Ἀμήν",
                "transliteration": "Amen (Verily / Truth)",
                "verse": "Revelation 3:14",
                "value": 99,
                "mnemonic": "99% Sure? No, 99 = AMEN (100% Truth & Affirmation)."
            }
        ]
    }
]


def print_memorization_dashboard():
    print("=" * 65)
    print("     GREEK ISOPSEPHY MEMORIZATION DASHBOARD (PEDAGOGICAL FRAMEWORK)     ")
    print("=" * 65)

    for cluster in pedagogical_database:
        print(f"\n>>> {cluster['category']} <<<")
        print("-" * 65)
        for item in cluster["items"]:
            calc_val = get_greek_isopsephy(item["greek"])
            print(f"• {item['greek']} ({item['transliteration']})")
            print(f"  VALUE    : {calc_val} (Location: {item['verse']})")
            print(f"  MEMORY HOOK: {item['mnemonic']}")
            print()


if __name__ == "__main__":
    print_memorization_dashboard()