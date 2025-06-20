# /alpha_core/phonetic_decoder.py

class PhoneticDecoder:
    def __init__(self):
        # Mini ARPAbet dictionary (seed set for bootstrapping)
        # Full CMUdict can be added later
        self.phoneme_dict = {
            "joey": ["JH", "OW", "IY"],
            "dog": ["D", "AO", "G"],
            "cat": ["K", "AE", "T"],
            "apple": ["AE", "P", "AH", "L"],
            "blue": ["B", "L", "UW"],
            "run": ["R", "AH", "N"],
            "quickly": ["K", "W", "IH", "K", "L", "IY"],
            "eat": ["IY", "T"],
            "sky": ["S", "K", "AY"],
            "happy": ["HH", "AE", "P", "IY"]
        }

    def transcribe(self, word_or_sentence):
        words = word_or_sentence.strip().lower().split()
        output = []

        for word in words:
            if word in self.phoneme_dict:
                output.append((word, self.phoneme_dict[word]))
            else:
                output.append((word, ["<UNK>"]))  # Unknown word

        return output

    def add_word(self, word, phonemes):
        """Allows dynamic learning of new phonemes"""
        if isinstance(phonemes, list) and all(isinstance(p, str) for p in phonemes):
            self.phoneme_dict[word.lower()] = phonemes
            return True
        return False

# Test Mode
if __name__ == "__main__":
    decoder = PhoneticDecoder()
    sample = "Joey eats an apple"
    result = decoder.transcribe(sample)
    for word, phonemes in result:
        print(f"{word.upper()}: {' '.join(phonemes)}")
