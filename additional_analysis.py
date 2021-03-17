import string

import nltk
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from bs4 import BeautifulSoup
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

emacs_df = pd.read_csv(r"emacs_scrape_result.csv")
vim_df = pd.read_csv(r"vim_scrape_result.csv")


def remove_html(text):
    soup = BeautifulSoup(text, features="html.parser")
    html_free = soup.get_text()
    return html_free


def remove_punctuation(text):
    #nopunct = "".join([c for c in text if c not in string.punctuation])
    nopunct = ''
    for c in text:
        if c in string.punctuation:
            c = " "
        nopunct += c
    return nopunct

stop_words=set(stopwords.words("english"))

#Tokenize selftext of emacs
emacs_text = ''
for word in emacs_df.selftext:
    word = str(word)
    word = word.lower()
    emacs_text += word
emacs_text = remove_punctuation(emacs_text)
emacs_text = remove_html(emacs_text)

emacs_tokenized_word = word_tokenize(emacs_text)
#print(emacs_tokenized_word)
emacs_filtered_text = []
for w in emacs_tokenized_word:
    if w not in stop_words:
        emacs_filtered_text.append(w)
ps = PorterStemmer()

emacs_stemmed_words=[]
for w in emacs_filtered_text:
    emacs_stemmed_words.append(ps.stem(w))
lem = WordNetLemmatizer()
emacs_lem_words=[]
for w in emacs_filtered_text:
    emacs_lem_words.append(lem.lemmatize(w))
#print(emacs_lem_words)
emacs_fdist = FreqDist(emacs_lem_words)
#print(emacs_fdist)
print("Emacs frequent words are:", emacs_fdist.most_common(10))
emacs_fdist.plot(30,cumulative=False, title="Emacs words in selftext")
plt.show()

#Word Cloud for emacs

wordcloud_stopwords = set(STOPWORDS)
wordcloud_stopwords.update(["or", "org", "https"])
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=wordcloud_stopwords,
                      min_font_size=10).generate(emacs_text)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.title("Word Cloud of vim")
plt.tight_layout(pad=0)

plt.show()


#Check positive, negative, or neural for a each text
sia = SIA()
results = []
texts = set()
for line in emacs_df.selftext:
    line = str(line)
    pol_score = sia.polarity_scores(line)
    pol_score['emacs_text'] = line
    results.append(pol_score)
df1 = pd.DataFrame.from_records(results)
print(df1.head())
df1.to_csv('emacs_positive_negative.csv')

#Tokenize selftext of vim
vim_text = ''
for word in vim_df.selftext:
    word = str(word)
    word = word.lower()
    vim_text += word
vim_text = remove_punctuation(vim_text)
vim_text = remove_html(vim_text)

vim_tokenized_word = word_tokenize(vim_text)
#print(vim_tokenized_word)
vim_filtered_text = []
for w in vim_tokenized_word:
    if w not in stop_words:
        vim_filtered_text.append(w)

vim_stemmed_words=[]
for w in vim_filtered_text:
    vim_stemmed_words.append(ps.stem(w))
vim_lem_words=[]
for w in vim_filtered_text:
    vim_lem_words.append(lem.lemmatize(w))
#print(vim_lem_words)
vim_fdist = FreqDist(vim_lem_words)
#print(vim_fdist)
print("Vim frequent words are:", vim_fdist.most_common(10))
plt.figure()
vim_fdist.plot(30,cumulative=False, title="Vim words in selftext")
plt.show()

#Word Cloud for vim
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=wordcloud_stopwords,
                      min_font_size=10).generate(vim_text)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.title("Word Cloud of vim")
plt.tight_layout(pad=0)

plt.show()


#Check positive, negative, or neural for a each text
sia = SIA()
results = []
for line in vim_df.selftext:
    line = str(line)
    pol_score = sia.polarity_scores(line)
    pol_score['vim_text'] = line
    results.append(pol_score)
df2 = pd.DataFrame.from_records(results)
print(df2.head())
df2.to_csv('vim_positive_negative.csv')
