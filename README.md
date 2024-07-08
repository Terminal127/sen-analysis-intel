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
