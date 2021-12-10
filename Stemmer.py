class Stemmer:

    def __init__(self):
        self.ends = ['ات', 'ان', 'ترین', 'تر', 'م', 'ت', 'ش', 'یی', 'ی', 'ها', 'ٔ', '‌ا', '‌', 'ۀ']
        self.verb_ends = ['ام', 'ای', 'ایم', 'اید', 'اند']

    def stem(self, word):
        if len(word) <4:
            return word.strip()
        for end in self.ends:
            if word.endswith(end):
                word = word[:-len(end)]
        return word.strip()
