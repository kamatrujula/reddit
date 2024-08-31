import pandas as pd
import praw
from praw.models import MoreComments
import json
import datetime

#print("Hello World")

reddit = praw.Reddit(
    client_id="write your id",
    client_secret="write your secret",
    password="write your password",
    user_agent="aitascraper",
    username="write your username",
)

#print(reddit.user.me())

reddit.read_only = True

query = 'AITA'
sub = 'AmITheAsshole'
sort = "top"
limit = 10

top_posts = reddit.subreddit(sub).search(query, sort = sort, limit = limit)
total_posts = list()
i=0

for post in top_posts:
    #print(vars(post))
    #print(post.created) gives unix timestamp i.e second since Jan 01 1970. (UTC)
    Id = i,
    Title = post.title,
    Score = post.score,
    Content = post.selftext
    # print(post.selftext)
    # print(Content)
    NumberOfComments = post.num_comments,
    Publish_Date = datetime.datetime.fromtimestamp(
        int(post.created)
        ).strftime('%Y-%m-%d %H:%M:%S'),
    Link = post.permalink,
    #print(Publish_Date)
    data_set = {
        "Id": Id[0],
        "Title": Title[0],
        "Score": Score[0],
        "Content": Content,
        "NumberOfComments": NumberOfComments[0],
        "PublishDate": Publish_Date[0],
        "Link":'https://www.reddit.com'+Link[0]
    }
    total_posts.append(data_set)
    i=i+1
    #print(data_set)

df = pd.DataFrame(total_posts)
df.to_csv('data.csv', sep=',', index=False)
json_string = json.dumps(total_posts)
jsonFile = open("data.json", "w")
jsonFile.write(json_string)
jsonFile.close()

print("Script executed successfully\n")
#run using 'python scrapingtool.py'
