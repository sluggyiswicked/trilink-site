#!/usr/bin/env python3
"""
Flexible image generation utility for the Hugo site
Usage: python image_generator.py
"""

import os
import requests
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_image(prompt, filename, size="1024x1024", quality="standard"):
    """
    Generate an image using OpenAI DALL-E
    
    Args:
        prompt (str): Description of the image to generate
        filename (str): Name for the saved file (include extension)
        size (str): Image size - "1024x1024", "1792x1024", or "1024x1792" 
        quality (str): "standard" or "hd"
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        print(f"Generating: {filename}")
        print(f"Size: {size}, Quality: {quality}")
        print(f"Prompt: {prompt}")
        print("-" * 60)
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality=quality,
            n=1,
        )
        
        image_url = response.data[0].url
        print(f"Generated URL: {image_url}")
        
        # Download and save the image
        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            # Ensure directory exists
            os.makedirs("static/images", exist_ok=True)
            
            with open(f"static/images/{filename}", "wb") as f:
                f.write(img_response.content)
            print(f"SUCCESS: Saved to static/images/{filename}")
            return True
        else:
            print(f"ERROR: Failed to download image (HTTP {img_response.status_code})")
            return False
            
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def main():
    """Interactive image generation"""
    print("=== Hugo Site Image Generator ===")
    print("Available sizes: 1024x1024 (square), 1792x1024 (landscape), 1024x1792 (portrait)")
    print("Available quality: standard, hd")
    print()
    
    while True:
        prompt = input("Enter image prompt (or 'quit' to exit): ").strip()
        if prompt.lower() in ['quit', 'exit', 'q']:
            break
            
        filename = input("Enter filename (e.g., 'hero-image.jpg'): ").strip()
        if not filename:
            filename = "generated-image.jpg"
            
        size = input("Enter size [1024x1024]: ").strip()
        if not size:
            size = "1024x1024"
            
        quality = input("Enter quality [standard]: ").strip() 
        if not quality:
            quality = "standard"
            
        print()
        success = generate_image(prompt, filename, size, quality)
        
        if success:
            print(f"✓ Image saved successfully!")
        else:
            print(f"✗ Failed to generate image")
        print("=" * 60)
        print()

if __name__ == "__main__":
    main()