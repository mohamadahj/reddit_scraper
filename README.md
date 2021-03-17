# reddit_scraper
In the scraper.py we scrape two subreddits: [r/emacs](https://www.reddit.com/r/emacs/) and [r/vim](https://www.reddit.com/r/vim/). We need [PushshiftAPI](https://github.com/pushshift/api) to scrape within a time period.
To install this package we need the following code:  
 ```pip install psaw ```  
 We scrape the subreddits within 3-month period ("01/2020-03/2020").
 Reddit uses [UNIX timestamps](Reddit uses UNIX timestamps to format date and time.) to format date and time. We use the datetime package to convert these entries.  
 We use pandas dataFrame to store results and convert them to csv files. Here's the code to install pandas:  
  ```pip install pandas ```  
We consider 5 metrics to analyze behaviour of contributors on [reddit](reddit.com). These metrics are:  
1. Score
2. Num_Comments
3. Date
4. Domain
5. Link_Flair_Text  

In the generate_plot.py we generate plots to understand the differences in distribution of the 5 metrics across the two sub-reddits. We use [matplotlib](https://matplotlib.org/) for generating plots.
Then in additional_analysis.py we do simple text mining to provide better understanding of differences in contributor behaviour. To do this, we use [nltk](www.nltk.org
) package. (For the first time, you need to run this code after importing nltk: ``` nltk.download() ``` )  
