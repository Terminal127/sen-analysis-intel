import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Configure Chrome options and specify not to run it headless
chromeOptions = uc.ChromeOptions()
chromeOptions.headless = False

# Create an instance of the Chrome WebDriver and enable subprocess support
driver = uc.Chrome(use_subprocess=True, options=chromeOptions)

# The URL of the Amazon product page
url = "https://www.amazon.in/Redmi-Jade-Black-6GB-128GB/product-reviews/B0C9JFWBH7"

def get_reviews(page_num):
    try:
        # Navigate to the review page
        page_url = f"{url}?pageNumber={page_num}"
        driver.get(page_url)

        # Wait for the reviews to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".review"))
        )

        # Extract the reviews
        reviews = []
        review_elements = driver.find_elements(By.CSS_SELECTOR, ".review")
        for review_element in review_elements:
            review = {}
            try:
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
                sub_reviews = [comment_element.text.strip() for comment_element in comment_elements]
                review['sub_reviews'] = sub_reviews

            except NoSuchElementException:
                # Continue if any element is not found
                continue

            reviews.append(review)
        
        return reviews

    except TimeoutException:
        print(f"Timeout waiting for reviews to load on page {page_num}")
        return []

# Open the output file
with open("reviews.txt", "w", encoding="utf-8") as file:
    for page_num in range(1, 6):  # Loop through 5 pages
        reviews = []
        retries = 3
        for _ in range(retries):
            reviews = get_reviews(page_num)
            if reviews:
                break
            time.sleep(3)  # Wait before retrying

        # Write the reviews to the file
        file.write(f"Page {page_num}:\n")
        for i, review in enumerate(reviews):
            file.write(f"Review {i+1}:\n")
            file.write(f" Rating: {review['rating']}\n")
            file.write(f" Content: {review['content']}\n")
            file.write(f" Variant: {review['variant']}\n")
            file.write(f" Name: {review['name']}\n")
            file.write(f" Date: {review['date']}\n")
            file.write(f" Verified: {review['verified']}\n")
            if review['sub_reviews']:
                file.write(" Sub-reviews:\n")
                for j, sub_review in enumerate(review['sub_reviews']):
                    file.write(f" Sub-review {j+1}: {sub_review}\n")
            file.write("-" * 20 + "\n")

# Close the WebDriver instance
driver.close()
