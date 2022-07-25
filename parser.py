import tika
tika.initVM()
from tika import parser
from nltk.tokenize import word_tokenize
data = parser.from_file('Documents/network-policy.pdf')
data = data['content']
#print('DATA:',word_tokenize(data[500:2000]))

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer
for i in data:
    print(i)
print('DATA_LEMMA:',lemmatizer.lemmatize(i'\n'))