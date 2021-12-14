class Normalizer:
    def __init__(self):
        self.arabic_alphabet = {'ﻱ': 'ی', 'ي': 'ی', 'ﻲ': 'ی', 'ﻙ': 'ک', 'ﻛ': 'ک', 'ﻜ': 'ک', 'ﻚ': 'ک', 'ﻋ': '', 'أ': 'ا',
                                'إ': 'ا',
                                'ئ': 'ی', 'ٔ': '', 'ؤ': 'و'}

        self.english_numbers = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷',
                                '8': '۸', '9': '۹'}
        self.characters = {'%': '٪', '-': ' '}

    def normalize(self, text):
        text = list(text.lower())
        for index in range(0, len(text)):
            if self.arabic_alphabet.get(text[index]) is not None:
                text[index] = self.arabic_alphabet.get(text[index])
            if self.english_numbers.get(text[index]) is not None:
                text[index] = self.english_numbers.get(text[index])
            if self.characters.get(text[index]) is not None:
                text[index] = self.characters.get(text[index])
        return ''.join(text)
