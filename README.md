# reddit_scraper
In the scraper.py I scrape two subreddits: [r/emacs](https://www.reddit.com/r/emacs/) and [r/vim](https://www.reddit.com/r/vim/). I need [PushshiftAPI](https://github.com/pushshift/api) to scrape within a time period.
To install this package, we need the following code:  
 ```pip install psaw ```  
 I scrape the subreddits within a 3-month period ("01/2020-03/2020").
 Reddit uses [UNIX timestamps](Reddit uses UNIX timestamps to format date and time.) to format date and time. I use the datetime package to convert these entries.  
 I use pandas dataFrame to store results and convert them to csv files. Here's the code to install pandas:  
  ```pip install pandas ```  
I consider 5 metrics to analyze the behavior of contributors on [reddit](reddit.com). These metrics are:  
1. Score
2. Num_Comments
3. Date
4. Domain
5. Author  

In the generate_plot.py, I generate plots to understand the differences in the distribution of the 5 metrics across the two subreddits. I use [matplotlib](https://matplotlib.org/) for generating plots.
Then in additional_analysis.py, I do simple text mining to provide a better understanding of differences in contributor behavior. To do this, I use [nltk](www.nltk.org
) package. (For the first time, you need to run this code after importing nltk: ``` nltk.download() ``` )  
In this code, I tokenize the selftext of each subreddits, remove unwanted words, Lemmatization and Stemming.  
I also do sentiment analysis for labeling each of the texts (labels are: positive, negative, and neural). I generate csv files for both subreddits containing the label of posts.
