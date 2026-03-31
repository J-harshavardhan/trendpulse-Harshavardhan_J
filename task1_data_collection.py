#Task 1: Fetch Data from Reddit API
#Fetches trending posts from 5 subreddits and saves them to a JSON file

import requests
import json
import os 
import time 
import datetime

# 5 Subreddits to fetch trending posts from :

SUBREDDITS = [ 'technology','worldnews', 'sports', 'science', 'entertainment']

# Reddit blocks requests without a User-Agent header :

REDDITS = {"User-Agent": "TrendPlus/1.0"}

# posts per Sub-Reddits :
limit = 25 

# Store all extracted posts here :
all_posts =[]

# ================ TASk - 1 ========================================================

for sub_reddits in SUBREDDITS:
    url = f"https://www.reddit.com/r/{sub_reddits}/hot.json?limit={limit}"
    print(f"Fetching r/{sub_reddits}...")

    try:
        response = requests.get(url, headers=REDDITS)
        #raises for error : 4xx / 5xx respomse
        response.raise_for_status()
        data = response.json()


        #===================== TASk - 2 ==============================================

        # Reddit nests post data inside : data -> childern -> [item] -> data

        posts= data['data']['children']

        for item in posts:
            # Actudal post content is inside "data" key :
            post = item['data']

            extracted = {
            # added manually :

                "post_id":      post.get("id"),
                "title":        post.get("title"),
                "subreddit":    post.get("subreddit"),
                "score":        post.get("score"),
                "num_comments": post.get("num_comments"),
                "author":       post.get("author"),
                "collected_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
            }
            all_posts.append(extracted)
        print(f" got {len(posts)} posts from r/{sub_reddits}")
    except requests.exceptions.RequestException as e :
         # If request fails, print and move on — don't crash the script
        print(f" Failed to fetch r/{sub_reddits} : {e}")
    
    time.sleep(2) # Wait 2 seconds

# ====================== TASK -3 =========================================================

# Create data / folder if it dosen't exist :
os.makedirs('data', exist_ok=True)

# Filename includes todays date 
F_N= datetime.datetime.now().strftime("%Y%m%d")
F_P = os.path.join("data", f"trends_{F_N}.json")

# File : 
with open(F_P, 'w', encoding="utf-8") as f :
    json.dump(all_posts, f , indent=2, ensure_ascii=False)

print(f"\nCollacted {len(all_posts)}, posts. Saved to {F_P}")