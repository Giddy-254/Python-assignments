import requests
import os
import hashlib
from urllib.parse import urlparse

def fetch_image(url, download_dir, downloaded_hashes):
    """
    Fetches a single image from the given URL and saves it to the specified directory.
    Prevents duplicates by checking file hashes.
    """

    try:
        # Fetch the image with timeout
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Security precaution: only proceed if Content-Type is an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (Not an image): {url}")
            return

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:  
            filename = "downloaded_image.jpg"

        filepath = os.path.join(download_dir, filename)

        # Calculate file hash to detect duplicates
        file_bytes = response.content
        file_hash = hashlib.md5(file_bytes).hexdigest()
        if file_hash in downloaded_hashes:
            print(f"✗ Duplicate skipped: {filename}")
            return
        downloaded_hashes.add(file_hash)

        # Save file
        with open(filepath, "wb") as f:
            f.write(file_bytes)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory if it doesn't exist
    download_dir = "Fetched_Images"
    os.makedirs(download_dir, exist_ok=True)

    # Get multiple URLs from user
    urls = input("Please enter image URLs (separate with spaces): ").split()

    # Track downloaded file hashes to prevent duplicates
    downloaded_hashes = set()

    for url in urls:
        fetch_image(url.strip(), download_dir, downloaded_hashes)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
