import nltk

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stop_words = set(stopwords.words("english"))

stop_words.remove("won")

ps = PorterStemmer()

def transform_text(text):

    # Lowercase
    text = text.lower()

    # Tokenize
    tokens = word_tokenize(text)

    # Remove non-alphanumeric and stopwords first, then do stemming
    cleaned_tokens =[]

    for token in tokens:
        if token.isalnum() and token not in stop_words:
            cleaned_tokens.append(ps.stem(token))

    # TfidfVectorizer and CountVectorizer expect text strings, not lists of tokens.  
    return " ".join(cleaned_tokens)


