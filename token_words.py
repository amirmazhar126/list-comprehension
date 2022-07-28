import nltk
from nltk.tokenize import word_tokenize
sentence = 'my name is amir','i live in lucknow','i love playing cricket'
tokenized = [(word_tokenize(a)) for a in sentence]
tokenized