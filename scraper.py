from psaw import PushshiftAPI
import datetime as dt
import pandas as pd

#Create an instance of PushshiftAPI
api = PushshiftAPI()
#Time period: 01/01/2020-31/03/2020
start_epoch = int(dt.datetime(2020, 1, 1).timestamp())
end_epoch = int(dt.datetime(2020, 4, 1).timestamp())
query = api.search_submissions(subreddit='emacs', after=start_epoch, before=end_epoch)
#Put the query on a list
emacs_submissions = list()
for element in query:
    emacs_submissions.append(element.d_)
#Save the list into a dataFrame
emacs_df = pd.DataFrame(emacs_submissions)
query2 = api.search_submissions(subreddit='vim', after=start_epoch, before=end_epoch)
vim_submissions = list()
for element in query2:
    vim_submissions.append(element.d_)
vim_df = pd.DataFrame(vim_submissions)

#Fix the date column
def get_date(submission):
    time = submission
    return dt.datetime.fromtimestamp(time)


timestamp = emacs_df["created"].apply(get_date)
emacs_df = emacs_df.assign(timestamp=timestamp)
timestamp2 = vim_df["created"].apply(get_date)
vim_df = vim_df.assign(timestamp=timestamp)

#Export into a csv file
emacs_df.to_csv('emacs_result.csv', sep=',', header=True, index=False, columns=[
    'id', 'author', 'timestamp', 'domain', 'url', 'title',
    'score', 'selftext', 'num_comments', 'num_crossposts'
])
vim_df.to_csv('vim_result.csv', sep=',', header=True, index=False, columns=[
    'id', 'author', 'timestamp', 'domain', 'url', 'title',
    'score', 'selftext', 'num_comments', 'num_crossposts'
])
