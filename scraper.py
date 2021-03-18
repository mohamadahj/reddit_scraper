from psaw import PushshiftAPI
import datetime as dt
import pandas as pd

#Create an instance of PushshiftAPI
api = PushshiftAPI()
#Time period: 01/01/2020-31/03/2020
s_time = dt.datetime(2020, 1, 1)
start_epoch = int(s_time.replace().timestamp())
e_time = dt.datetime(2020, 4, 1)
end_epoch = int(e_time.replace().timestamp())
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


timestamp = emacs_df["created_utc"].apply(get_date)
emacs_df = emacs_df.assign(datetime=timestamp)
timestamp2 = vim_df["created_utc"].apply(get_date)
vim_df = vim_df.assign(datetime=timestamp2)
print("Exporting emacs data to emacs_scrape_result.csv")
#Export into a csv file
emacs_df.to_csv('emacs_scrape_result.csv', sep=',', header=True, index=False, columns=[
    'id', 'author', 'datetime', 'domain',
    'score', 'num_comments', 'title', 'selftext'
])
print("Exporting vim data to vim_scrape_result.csv")
vim_df.to_csv('vim_scrape_result.csv', sep=',', header=True, index=False, columns=[
    'id', 'author', 'datetime', 'domain',
    'score', 'num_comments', 'title', 'selftext'
])
