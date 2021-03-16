from psaw import PushshiftAPI
import datetime as dt
import pandas as pd

api = PushshiftAPI()
start_epoch = int(dt.datetime(2020, 1, 1).timestamp())
end_epoch = int(dt.datetime(2020, 4, 1).timestamp())
query = api.search_submissions(subreddit='emacs', after=start_epoch, before=end_epoch)
emacs_submissions = list()
for element in query:
    emacs_submissions.append(element.d_)
emacs_df = pd.DataFrame(emacs_submissions)


def get_date(submission):
    time = submission
    return dt.datetime.fromtimestamp(time)


timestamp = emacs_df["created"].apply(get_date)
emacs_df = emacs_df.assign(timestamp=timestamp)

emacs_df.to_csv('emacs_result.csv', sep=',', header=True, index=False, columns=[
    'id', 'author', 'timestamp', 'domain', 'url', 'title',
    'score', 'selftext', 'num_comments', 'num_crossposts'
])
