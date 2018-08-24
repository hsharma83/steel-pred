import pandas as pd
import nltk
from nltk.corpus import stopwords
from datetime import date,timedelta,datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia = SIA()
nltk.download('vader_lexicon')

metal = pd.read_csv('metaljunction.csv')
orb = pd.read_csv('steelorbis.csv')
mint = pd.read_csv('steelnews.csv')

#formatting for metaljunction file
metal = metal[pd.notnull(metal['date'])]
metal = metal[metal.title != 'title']
metal['date'] = pd.to_datetime(metal.date).dt.date

#formatting for orbis file
orb = orb[orb.date != 'date']
orb['date'] = pd.to_datetime(orb.date).dt.date

#formatting for mint file
mint = mint[mint.date != 'date']
mint['date'] = pd.to_datetime(mint.date).dt.date

#merging
news = [metal, orb, mint]
news = pd.concat(news)

td_day = timedelta(days=2)
today = date.today()
news = news[news.date > (today - td_day)] #removing old news

news['title'] = news['title'].str.lower()
news['title'] = news['title'].str.replace('[^\w\s]','')
news['title'] = news['title'].str.replace('\d+','')
stop = stopwords.words('english')
news['title'] = news['title'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

#merging date wise
news = news.sort_values(['date']).groupby('date',sort=False).title.apply(' '.join).reset_index()

#sentiment analysis
news['senti'] = news['title'].apply(sia.polarity_scores)
news = pd.concat([news,pd.DataFrame(news['senti'].tolist())],axis=1)

news.to_csv('news.csv',index=False)
