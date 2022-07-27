from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
porter = PorterStemmer()
list1=['telling','swimming','wired']
stem_words=[porter.stem(x) for x in list1]
stem_words