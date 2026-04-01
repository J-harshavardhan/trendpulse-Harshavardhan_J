# TrendPulse - Task 3: Analysis with Pandas and NumPy
# firstly Loads clean CSV from Task 2 and  computes stats, adds new columns, saves result

import pandas as pd
import numpy as np

#================= TASK - 1 =======================================================================

df=pd.read_csv("data/trends_clean.csv")

print(f"Loaded data : {df.shape}")

print("\nFirst 5 Rows : ")
print(df.head())

# Average score and comments acrosss all posts

avg_score=df['score'].mean()
avd_comments=df['num_comments'].mean()

print(f"\nAverage Score : {avg_score:,.0f}")
print(f"\nAverage Comments : {avd_comments:,.0f}")

#=============== TASK - 2 : numpy Statistics ======================================
# convert to NumPy array for calculations
scores=df['score'].to_numpy()
print("\n-------- NUMPY STATS --------")
print(f"Mean Score  : {np.mean(scores):,.0f}")  # mean value of scores
print(f"Median Score : {np.median(scores):,.0f}") # median value of scores
print(f"Std Score  : {np.std(scores):,.0f}") # std value of scores
print(f"Max Score  : {np.max(scores):,.0f}") # max value of scores
print(f"Min Score  : {np.min(scores):,.0f}") # min value of scores

# Subreddit with the most posts :
top_subreddit = df['subreddit'].value_counts().idxmax()
top_count     = df['subreddit'].value_counts().max()

print(f"\nMost posts from {top_subreddit} ({top_count} posts)")

# Post with the most comments :
most_commented = df.loc[df['num_comments'].idxmax()]
print(f'\nMost commented post : "{most_commented['title']}"  --{most_commented['num_comments']} comments')

#========== TASK - 3 : Add new columns =====================================================================
# engagement = how much discussion a post generates per upvote
# adding 1 to score avoids division by zero
df['engagement'] = df['num_comments'] / (df['score'] + 1)

# is_popular = True if score is above the average score
df['is_popular'] = df['score'] > avg_score

#================== TASK - 4 : Save the Result ============================================================
output_path='data/trends_analysed.csv'
df.to_csv(output_path,index=False)
print(f"\nSaved to { output_path}")