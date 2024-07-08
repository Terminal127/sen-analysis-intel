# Intel Products Sentiment Analysis

This project analyzes customer sentiment towards Intel products using a multi-stage approach:

## Project Overview

1. **Data Gathering**: Web scraping customer reviews from Amazon using Selenium.

2. **Sentiment Analysis & Visualization**:
   - Data cleaning
   - Dual sentiment analysis: NLTK's VADER and Hugging Face Transformers (BERTweet)
   - Visualization of sentiment distribution

3. **Aspect-Based Sentiment Analysis (ABSA)**:
   - Identify problematic aspects in negative reviews using spaCy
   - Analyze aspect-specific sentiment with a fine-tuned DeBERTa model

4. **Insights and Actionable Recommendations**:
   - Provide deep understanding of customer feedback
   - Guide product improvements, marketing strategies, and customer support

# Python Script:

**The script defines a main function that takes various parameters such as the URL of the Amazon product review page, the number of pages to scrape, the output CSV file name, wait time for elements to load, the number of retries, and an optional proxy server address.**:
- The script sets up a headless browser using Selenium to navigate to the given URL and scrape reviews from the specified number of pages.
- The scraped reviews are saved to a CSV file.

# links.txt File:

**This file contains a list of URLs, each pointing to an Amazon product review page.**


## Files
- `Intel_Products_Sentiment_Analysis_RoBERTa.ipynb`: Jupyter Notebook with analysis
- `reviews.csv`: Dataset of reviews

## Instructions
1. **Data Cleaning**: Remove missing values and clean text
2. **Sentiment Analysis**: Use RoBERTa model for sentiment analysis
3. **Insights and Recommendations**: Provide actionable insights based on analysis

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/Terminal127/sen-analysis-intel.git
   ```
2. Navigate to the project directory:
   ```sh
   cd sen-analysis-intel
   ```
3. Open the Jupyter Notebook:
   ```sh
   jupyter notebook Intel_Products_Sentiment_Analysis_RoBERTa.ipynb
   ```
