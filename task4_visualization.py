# TrendPulse - Task 4 : Visualizations
# Loads the analysed CSV from Task 3 and creates 3 charts + a dashboard

import pandas as pd
import matplotlib.pyplot as plt 
import os

#================ TASK - 1 : Setup =========================================================

df=pd.read_csv('data/trends_analysed.csv')

#  Create outputs/ folder
# if it dosen't exist :

os.makedirs("outputs", exist_ok=True)

# ************* Chart 1 : Top 10 Posts by Score ********************************************
# sort by score and take top 10 :
Top_10 = df.nlargest(10 , 'score').copy()

# Shorten titles longer than 50 characters for readability
Top_10['short_title'] = Top_10['title'].apply(
    lambda titles: titles[:50] + "...." if len(titles) > 50 else titles
)

fig1, ax1 = plt.subplots(figsize=(10,6))
ax1.barh(Top_10['short_title'] , Top_10['score'] , color="steelblue")
ax1.set_xlabel("Score ")
ax1.set_ylabel("Story Title")
ax1.set_title("Top 10 Stories by score")

# Highest score at top :
ax1.invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.show()
print("Saved chart1_top_stories.png")

# ************** Chart - 2 : Stories per Category **************************************
subreddit_counts = df['subreddit'].value_counts()
colors=["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6"]

fig2,ax2 = plt.subplots(figsize=(8,5))
ax2.bar(subreddit_counts.index , subreddit_counts.values , color = colors)
ax2.set_xlabel('Category')
ax2.set_ylabel('Number per Category')
ax2.set_title("Stories per Category")
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.show()
print("Saved chart2_categories.png")

# ************** Chart - 3 : Score vs Comments **************************************

# separate popular and non-popular posts for different colours 
popular = df[df['is_popular'] == True ] 
not_popular = df[df['is_popular'] == False ] 

fig3 , ax3 = plt.subplots(figsize=(8,6))
ax3.scatter(not_popular['score']  , not_popular['num_comments'],
            color= 'gray' , alpha=0.6 , label='Not Popular'
            )
ax3.scatter(popular['score']  , popular['num_comments'],
            color= 'red' , alpha=0.7 , label='Popular'
            )
ax3.set_xlabel("Score ")
ax3.set_ylabel("Number of comments ")
ax3.set_title("Score vs Comments ")
ax3.legend()
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.show()
print("Saved chart3_scatter.png")


#**************** Bonus : DashBoard ********************************

fig, axes = plt.subplots(1,3,figsize=(20,6))
fig.suptitle("TrendPulse Dashboard " , fontsize = 16 , fontweight = "bold")


#  @ Chart - 1 (In Dashboard) :
axes[0].barh(Top_10['short_title'] , Top_10["score"] , color = 'steelblue')
axes[0].set_title("Top 10 Stories by Score")
axes[0].set_xlabel("score")
axes[0].invert_yaxis()

#  @ Chart - 2 (In Dashboard) :
axes[1].bar(subreddit_counts.index, subreddit_counts.values  , color = colors)
axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")

#  @ Chart - 3 (In Dashboard) :
axes[2].scatter(not_popular["score"] , not_popular["num_comments"] ,
               color ="gray" , alpha=0.6 , label='Not Popular'
               )
axes[2].scatter(popular["score"] , popular["num_comments"] ,
               color ="red" , alpha=0.7 , label='Popular'
               )
axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Comments")
axes[2].legend()

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()
print("Saved dashboard.png")