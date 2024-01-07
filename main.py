from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download('punkt')

url = 'https://www.voanews.com/a/unc-members-reaffirm-defense-of-south-korea-china-remains-opposed-/7360382.html'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity

if sentiment == 0 :
    print('Neutral')
elif sentiment > 0:
    print('Positive')
else:
    print('Negative') 
