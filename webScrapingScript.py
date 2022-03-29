#https://medium.com/swlh/how-to-scrape-large-amounts-of-reddit-data-using-pushshift-1d33bde9286

from tracemalloc import start
import pandas as pd 
import datetime as dt
from pmaw import PushshiftAPI

api = PushshiftAPI()


firstMarkerStart = int(dt.datetime(2019,9,1,0,0).timestamp())
firstMarkerEnd = int(dt.datetime(2019,12,31,0,0).timestamp())

secondMarkerStart = int(dt.datetime(2020,1,15,0,0).timestamp())
secondMarkerEnd = int(dt.datetime(2020,5,18,0,0).timestamp())

thirdMarkerStart = int(dt.datetime(2020,9,1,0,0).timestamp())
thirdMarkerEnd = int(dt.datetime(2020,12,31,0,0).timestamp())

fourthMarkerStart = int(dt.datetime(2021,1,15,0,0).timestamp())
fourthMarkerEnd = int(dt.datetime(2021,5,18,0,0).timestamp())

fifthMarkerStart = int(dt.datetime(2021,9,1,0,0).timestamp())
fifthMarkerEnd = int(dt.datetime(2021,12,31,0,0).timestamp())

before = int(dt.datetime(2019,12,31,0,0).timestamp())
after = int(dt.datetime(2019,9,1,0,0).timestamp())

startMarkers = [firstMarkerStart, secondMarkerStart, thirdMarkerStart, fourthMarkerStart, fifthMarkerStart]
endMarkers = [firstMarkerEnd, secondMarkerEnd, thirdMarkerEnd, fourthMarkerEnd, fifthMarkerEnd]



# subreddit = "NEU"
sems = ["f19","s20","f20","s21", "f21"]
subreddits = ["uofm", "UNC"]

limit=1000
for subreddit in subreddits:
    for i in range(0,len(sems)):
        posts = api.search_submissions(subreddit=subreddit, limit=limit, before=endMarkers[i], after=startMarkers[i])
        posts_df = pd.DataFrame(posts)
        posts_df_clean = posts_df[['title','selftext', 'created_utc','score','total_awards_received']]
        posts_df_clean.to_csv(f'./csv/{subreddit}_{sems[i]}_posts.csv', header=True, index=False, columns=list(posts_df_clean.axes[1]))

        comments = api.search_comments(subreddit=subreddit, limit=limit, before=endMarkers[i], after=startMarkers[i])
        comments_df = pd.DataFrame(comments)
        comments_df_clean = comments_df[['body', 'created_utc','score','total_awards_received']]
        comments_df_clean.to_csv(f'./csv/{subreddit}_{sems[i]}_comms.csv', header=True, index=False, columns=list(comments_df_clean.axes[1]))

