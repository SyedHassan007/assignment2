import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

# Function to scrape images from a webpage
def scrape_images_from_webpage(url, output_dir="images"):
    """
    Scrape images from the given webpage and save them locally.
    
    Args:
        url (str): The webpage URL.
        output_dir (str): Directory to save images.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Send an HTTP GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all <img> tags
        img_tags = soup.find_all('img')
        print(f"Found {len(img_tags)} images on the page.")

        # Download each image
        for img_tag in img_tags:
            # Get the image URL
            img_url = img_tag.get('src')
            if not img_url:
                continue  # Skip if no URL found

            # Convert relative URLs to absolute URLs
            img_url = urljoin(url, img_url)
            print(f"Downloading image: {img_url}")

            # Retrieve and save the image
            img_data = requests.get(img_url).content
            img_name = os.path.basename(img_url)
            img_path = os.path.join(output_dir, img_name)

            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)
                print(f"Saved: {img_path}")
        
        print("Image scraping completed.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # URL of the webpage to scrape
    webpage_url = "https://www.wikipedia.org/"  
    scrape_images_from_webpage(webpage_url)
