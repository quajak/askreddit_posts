#use custom search from https://redditsearch.io/?term=&dataviz=false&aggs=false&subreddits=askreddit&searchtype=posts&search=true&start=1546318800&end=1546405200&size=100000
#https://redditsearch.io/
from datetime import timedelta, datetime
import requests
import json
import praw
import time
import sys
import os.path

def save_posts(start, end):
    if path.exists(str(int(datetime.timestamp(start))) + "data.json"):
        print("Skipping" + str(start) + "as it exists")
        return
    search_query = "https://api.pushshift.io/reddit/search/submission/?q=&after=" + str(int(datetime.timestamp(start))) + "&before=" + str(int(datetime.timestamp(end))) + "&subreddit=askreddit&author=&aggs=&metadata=true&frequency=hour&advanced=false&sort=desc&domain=&sort_type=num_comments&size=1000"
    print(search_query)

    cookies = {"__cfduid":"d6d169f3395075c76dea71204165c83c41575582391"}
    r = requests.get(search_query, cookies=cookies)
    data = json.loads(r.text)["data"]

    posts = []
    c = 0
    for d in data:
        c += 1
        if c % 50 == 0:
            print("Finished " + str(c) + " posts")
        try:
            post = user_agent.submission(d["id"])
            s = post.score
            posts.append([d["title"], d["score"], d["num_comments"], s, post.link_flair_text])
        except Exception e:
            with open("error" + str(int(datetime.timestamp(start))) + ".txt", "w") as f:
                f.write(str(e))
    print("Got " + str(len(posts)) + " posts")
    with open(str(int(datetime.timestamp(start))) + "data.json", "w") as f:
        json.dump(posts, f)

print("starting")
user_agent = praw.Reddit(client_id='test',
                     client_secret='test',
                     user_agent='get askreddit', username="test",password="test")
user_agent.read_only = True
if len(sys.argv) == 4:
    s_year = int(sys.argv[1])
    s_month = int(sys.argv[2])
    s_day = int(sys.argv[3])
else:
    print(sys.argv)
    print("Start year:")
    s_year = int(input())
    print("Start month: ")
    s_month = int(input())
    print("Start day: ")
    s_day = int(input())
start = datetime(s_year, s_month, s_day, 0, 0, 0)
step_size = 4 # hours
for i in range(6):
    end = start + timedelta(hours=4)
    s_time = time.time()
    save_posts(start, end)
    print("Finished 4 hours in " + str(time.time() - s_time))
    start = end
print("Finished!!")