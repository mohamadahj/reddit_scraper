from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(r"emacs_result.csv", encoding="latin-1")

comment_words = ''
stopwords = set(STOPWORDS)
stopwords.update(["or", "org", "https"])

text = ''
# iterate through the csv file
for val in df.selftext:

    # typecaste each val to string
    val = str(val)
    #tokenized_word = word_tokenize(val)
    # split the value
    tokens = val.split()
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    comment_words += " " .join(tokens) + " "
    text += " " .join(val) + " "
#tokenized_word = word_tokenize(df.selftext + " ")
print(text)
#tokenized_word = word_tokenize("Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.")
fdist = FreqDist(text)
print(fdist)
print(fdist.most_common(2))
fdist.plot(30,cumulative=False)
plt.show()
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

#plt.show()