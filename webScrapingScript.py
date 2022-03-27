#https://medium.com/swlh/how-to-scrape-large-amounts-of-reddit-data-using-pushshift-1d33bde9286

import pandas as pd 
import datetime as dt
from pmaw import PushshiftAPI

api = PushshiftAPI()

firstMarkerStart = int(dt.datetime(2019,9,1).timestamp())
firstMarkerEnd = int(dt.datetime(2019,12,31).timestamp())

secondMarkerStart = int(dt.datetime(2020,1,15).timestamp())
secondMarkerEnd = int(dt.datetime(2020,5,18).timestamp())

thirdMarkerStart = int(dt.datetime(2020,9,1).timestamp())
thirdMarkerEnd = int(dt.datetime(2020,12,31).timestamp())

fourthMarkerStart = int(dt.datetime(2021,1,15).timestamp())
fourthMarkerEnd = int(dt.datetime(2021,5,18).timestamp())

fifthMarkerStart = int(dt.datetime(2021,9,1).timestamp())
fifthMarkerEnd = int(dt.datetime(2021,12,31).timestamp())

subreddit = " 
