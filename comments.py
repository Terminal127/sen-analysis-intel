from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Replace with the actual URL of the product review page
url = "https://www.amazon.in/Redmi-Jade-Black-6GB-128GB/product-reviews/B0C9JFWBH7"

# Replace with the path to your chromedriver executable

# Initialize the webdriver
driver = webdriver.Chrome()

# Navigate to the review page
driver.get(url)

# Wait for the reviews to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".review"))
    )
except TimeoutException:
    print("Timeout waiting for reviews to load")

# Extract the reviews
reviews = []
for review_element in driver.find_elements(By.CSS_SELECTOR, ".review"):
    review = {}

    # Extract the rating
    rating_element = review_element.find_element(By.CSS_SELECTOR, ".review-rating")
    review['rating'] = rating_element.text.strip()

    # Extract the review content
    review_content_element = review_element.find_element(By.CSS_SELECTOR, ".review-text-content")
    review['content'] = review_content_element.text.strip()

    # Extract the variant purchased
    variant_element = review_element.find_element(By.CSS_SELECTOR, ".review-format-strip")
    review['variant'] = variant_element.text.strip()

    # Extract the reviewer name
    name_element = review_element.find_element(By.CSS_SELECTOR, ".a-profile-name")
    review['name'] = name_element.text.strip()

    # Extract the review date
    date_element = review_element.find_element(By.CSS_SELECTOR, ".review-date")
    review['date'] = date_element.text.strip()

    # Determine if the review is verified or not
    verified_element = review_element.find_element(By.CSS_SELECTOR, ".a-color-state.a-text-bold")
    review['verified'] = 'Verified Purchase' in verified_element.text

    # Extract the sub-reviews (comments)
    comment_elements = review_element.find_elements(By.CSS_SELECTOR, ".review-comments .review-comment-content")
    sub_reviews = []
    for comment_element in comment_elements:
        sub_reviews.append(comment_element.text.strip())
    review['sub_reviews'] = sub_reviews

    reviews.append(review)

# Print the reviews
for i, review in enumerate(reviews):
    print(f"Review {i+1}:")
    print(f"  Rating: {review['rating']}")
    print(f"  Content: {review['content']}")
    print(f"  Variant: {review['variant']}")
    print(f"  Name: {review['name']}")
    print(f"  Date: {review['date']}")
    print(f"  Verified: {review['verified']}")
    if review['sub_reviews']:
        print("  Sub-reviews:")
        for j, sub_review in enumerate(review['sub_reviews']):
            print(f"    Sub-review {j+1}: {sub_review}")
    print("-" * 20)

# Close the webdriver
driver.quit()