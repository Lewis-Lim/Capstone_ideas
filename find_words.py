import re
import nltk
from nltk.corpus import words

# Download the official dictionary list (only downloads once)
nltk.download("words", quiet=True)

# Load valid English words into a set for O(1) fast lookup
ENGLISH_WORDS = set(word.lower() for word in words.words())


def find_embedded_words(text: str, target_lengths=(3, 4, 5, 6)) -> dict:
    """Scans a continuous string for valid English words of specified lengths.

    :param text: The input string containing uninterrupted letters.
    :param target_lengths: Tuple of word lengths to search for.
    :return: Dictionary grouping found unique words by their length.
    """
    # Clean non-alphabetic characters and convert to lowercase
    clean_text = re.sub(r"[^a-zA-Z]", "", text).lower()

    results = {length: set() for length in target_lengths}
    text_length = len(clean_text)

    # Slide a window across the string for each target length
    for length in target_lengths:
        for i in range(text_length - length + 1):
            substring = clean_text[i : i + length]
            if substring in ENGLISH_WORDS:
                results[length].add(substring)

    # Return sorted lists for each word length
    return {k: sorted(list(v)) for k, v in results.items()}


# --- EXAMPLE USAGE ---
if __name__ == "__main__":
    sample_text = """
    PaTsoCJTatsiCJwaaPwtoadGtyapfGoFatLJCItmGiamroyaiepomfyammpwjboypitgftfdunAIasotthwbagwiywbitcatdoJCIirfmtftwayabIhyimhfyaapwmogbimiaitdacotgFGimwhIyfyawtaoCJAiimptylmamamwkaadstymawieasbpabftdoCfwtfortctJCttgapoGIwytkbtwhhtmhrstatgstihbkttwigatatrtmiifCAmotbhbcitLbmiammbtstwwfSipCfearbofgwTldioolktIaphftdotgTfpCoosansbttamimiWtOtiewwipoitCipaitIrYaIwrfIkttypathotSoJCtwtofmdaiimeeahtIwnbaaabtwfcnaaCwbhimbwblobdFtmtliCatdigIIatlitftmflfmYwIscIctIahpbttMditdabwCftifbBtritfimnoyaCotIktIwracwyafypajitfstimymhactgiCJbomctyaOlymolbwotgoCstwIcasyoaaImhoytyasfioswomssbsftfotganfiabyoTiacsttotdboysatfGFihbgtytftsoCysnobihbasfhseitsctysIhanhtIsh
    """

    found_words = find_embedded_words(sample_text, target_lengths=(3, 4, 5, 6))

    for length, word_list in found_words.items():
        print(f"\n--- {length}-Letter Words ({len(word_list)} found) ---")
        print(", ".join(word_list))