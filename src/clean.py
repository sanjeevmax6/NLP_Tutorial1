import re
from nltk.corpus import stopwords

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;.]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))
SHORTWORD = re.compile(r'\W*\b\w{1,3}\b')

stop_words_lst = ['cell','spectral','data','double','bond','barrier','soluble', 'cells', 'performed using']


def clean_text(text):
    # Text must be a string and it should return the modified version by cleaning considering the above criteria

    text = str(text).lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    text = BAD_SYMBOLS_RE.sub('', text)
    text = re.sub(r'\b[a-zA-Z]\b','',str(text))
    text = re.sub('\d+','',text) 
    text = SHORTWORD.sub('',text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) 

    for w in stop_words_lst:
        pattern = r'\b'+w+r'\b'
        text = re.sub(pattern, '', str(text))

    return text