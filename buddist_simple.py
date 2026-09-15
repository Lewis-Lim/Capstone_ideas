import random

BUDDHIST_QUOTES = [
    ("मनोपुब्बङ्गमा धम्मा मनोगेट्ठा मनोमया।", "Mind precedes all mental states; mind is their chief."),
    ("न हि वेरेन वेरानि सम्मन्तीध कुदाचनम्।", "Hatred is never appeased by hatred; by love alone it ceases."),
    ("अप्पमादो अमटपदं पमादो मच्चुनो पदम्।", "Heedfulness is the path to the Deathless; heedlessness leads to death."),
    ("अत्ता हि अत्तनो नाथो को हि नाथो परो सिया।", "One is truly one's own protector; who else could protect you?"),
    ("अरोग्यपरमा लाभा सन्तुट्ठिपरमं धनम्।", "Health is the greatest gain; contentment is the greatest wealth."),
    ("सब्वे सङ्खारा अनिच्चाति यदा पञ्ञाय पस्सति।", "All conditioned things are impermanent; seeing this brings peace."),
]

quote = random.choice(BUDDHIST_QUOTES)
print(f"Original: {quote[0]}")
print(f"English:  \"{quote[1]}\"")