# TrendPulse - Task 2: Clean the Data and Save as CSV
# Loads the JSON from Task 1, cleans it, and saves as a tidy CSV file

import pandas as pd
import glob
import os

# ============================ TASK - 1 =====================================
# Find the most recent trends JSON() file in the data/ ->(folder) 
json_files=glob.glob('data/trends_*.json')
if not json_files:
    print(" NO JSON File found.. Run task1_data_collection.py first.....")
    exit()

# Pick the largest file by name ( Data is in the Filename)
latest_file = sorted(json_files)[-1]
df=pd.read_json(latest_file)
print(f"Loaded {len(df)} posts from {latest_file}")


#====================== TASK - 2 ==================================================

# remove duplicates based on post id
df.drop_duplicates(subset='post_id' )
print(f"After removing duplicates: {len(df)}")

# Drop rows where essential fields are missing values 

df.dropna(subset=['post_id','title','score'])

df.dropna(subset=['post_id','title','score'] )

print(f"After removing nulls: {len(df)}")

#Data types — make sure score and num_comments are integers
df['score']= df['score'].astype(int)
df['num_comments'] = df['num_comments'].astype(int)

#Low quality — remove posts where score is less than 5
df = df[ df['score'] >= 5 ]
print(f"After removing low scores : {len(df)}")

#Whitespace — strip extra spaces from the title column
df['title'] = df['title'].str.strip()

# Reset index after all the filtering
df.reset_index(drop=True,inplace=True)

#========================== TASK - 3 ========================================

output_path= 'data/trends_clean.csv'
df.to_csv(output_path,index=False)
print(f"\nSaved {len(df)} rows to {output_path}")

# Print how many posts came from the each sub_reddit
print("\nPosts per SubReddit:")
print(df['subreddit'].value_counts().to_string())
