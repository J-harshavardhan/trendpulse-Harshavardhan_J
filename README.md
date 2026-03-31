# 🚀 TrendPulse

### Reddit Trends Data Pipeline (Mini Project – AIML)

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Project Type](https://img.shields.io/badge/Type-Data%20Pipeline-orange)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

---

## 📌 Project Overview

**TrendPulse** is a mini data engineering and analytics project developed under the **AIML program (IIT Patna × Masai School)**.

It implements a **data pipeline** that extracts trending data from Reddit, processes it into structured format, and prepares it for analytics and visualization.

This project simulates a **real-world data workflow** used in:

* Social media analytics
* Trend detection systems
* Data-driven decision making

---

## 🎯 Problem Statement

Social media platforms generate massive unstructured data, but:

* Data is noisy and inconsistent
* APIs return nested JSON
* Raw data is not analysis-ready

**Solution:**
Build a pipeline to:

1. Extract data from Reddit
2. Transform it into structured format
3. Store it for analysis and visualization

---

## 🏗️ System Architecture

```
Reddit API
    ↓
Data Collection (requests)
    ↓
JSON Processing
    ↓
Structured Dataset
    ↓
Storage (JSON / CSV)
    ↓
Analysis (Pandas / NumPy)
    ↓
Visualization (Matplotlib / Seaborn)
```

---

## 🛠️ Tech Stack

| Layer           | Tools Used                       |
| --------------- | -------------------------------- |
| Language        | Python 3.14                      |
| Data Collection | requests                         |
| Data Processing | Pandas, NumPy *(upcoming)*       |
| Storage         | JSON, CSV                        |
| Visualization   | Matplotlib, Seaborn *(upcoming)* |

---

## 📂 Project Structure

```
trendpulse-Harshavardhan_J/
│
├── task1_data_collection.py
├── data/
│   └── trends_YYYYMMDD.json
├── README.md
```

---

## ⚙️ Features

### 🔹 Task 1 — Data Collection

* Fetches trending posts from:

  * r/technology
  * r/worldnews
  * r/sports
  * r/science
  * r/entertainment

* Extracted Fields:

  * Post ID
  * Title
  * Subreddit
  * Score
  * Comments
  * Author
  * Timestamp

* Includes:

  * API handling
  * Rate limiting (2 seconds)
  * Error handling

---

## ▶️ How to Run

### 1. Clone Repository

```
git clone https://github.com/J-harshavardhan/trendpulse-Harshavardhan_J.git
cd trendpulse-Harshavardhan_J
```

### 2. Install Dependencies

```
pip install requests
```

### 3. Run Script

```
python task1_data_collection.py
```

---

## 📊 Output

Stored in:

```
data/trends_YYYYMMDD.json
```

### Sample Data

```json
{
  "post_id": "xyz123",
  "title": "AI is transforming the future",
  "subreddit": "technology",
  "score": 2100,
  "num_comments": 450,
  "author": "user_abc",
  "collected_at": "2026-04-01 23:10:00"
}
```

---

## 📈 Future Enhancements

### 🔹 Task 2 — Clean the Data & Save as CSV

* Handle missing values
* Remove duplicate records
* Standardize formats
* Convert JSON → CSV
* Prepare ML-ready dataset

---

### 🔹 Task 3 — Analysis with Pandas & NumPy

* Perform Exploratory Data Analysis (EDA)
* Identify:

  * Most active subreddits
  * Highest engagement posts
  * User interaction trends
* Apply statistical operations

---

### 🔹 Task 4 — Visualizations

* Bar charts → Top subreddits
* Line charts → Trend over time
* Pie charts → Data distribution
* Tools:

  * Matplotlib
  * Seaborn
* Optional: Streamlit dashboard

---

## 📈 Complexity

* **Time Complexity:** O(S × L)

  * S = number of subreddits
  * L = posts per subreddit

---

## 🎓 Learning Outcomes

* API integration
* JSON parsing
* Data pipeline design
* Data preprocessing
* Preparation for ML workflows

---

## 👤 Author

**Harshavardhan J**
AIML Student – IIT Patna × Masai School
GitHub: https://github.com/J-harshavardhan

---

## ⭐ Contribution / Feedback

Suggestions and improvements are welcome!

---

## 📜 License

For academic and educational use only.

---
