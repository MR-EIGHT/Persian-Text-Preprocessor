from preper import Stemmer
from preper import Normalizer
from preper import Tokenizer
from preper import Wikipedia

stemmer = Stemmer()
print(stemmer.stem("گفتۀ"))
print(stemmer.stem("نویسنده هایش"))
print(stemmer.stem("نویسندگان"))
print(stemmer.stem("ستودگان"))
print(stemmer.stem("رفته ایم"))

normalizer = Normalizer()
print(normalizer.normalize("123 علیﻚ سلام"))
print(normalizer.normalize("كي به کی"))

tokenizer = Tokenizer()
print(tokenizer.tokenize(
    "علی و حسن، به مدرسه رفتند. و در راه بازگشت به خانه دوستانِ قدیمی شان را دیدند. آیا آنها خوشحال شدند؟ یا خیر؟! "
    "می‌خواهم بدانم."))

# wiki = Wikipedia("./data/fawiki-20211101-abstract.xml")
# print(len(wiki.doc_store))






