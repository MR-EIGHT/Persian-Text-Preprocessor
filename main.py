from Stemmer import Stemmer
from Normalizer import Normalizer

stemmer = Stemmer()
print(stemmer.stem("گفتۀ"))
print(stemmer.stem("نویسنده هایش"))

nor = Normalizer()
print(nor.normalize("123 علیﻚ سلام"))
print(nor.normalize("كي به کی"))

