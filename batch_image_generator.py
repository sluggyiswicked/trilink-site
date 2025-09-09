#!/usr/bin/env python3
"""
Batch image generation utility for hero backgrounds
Usage: python batch_image_generator.py
"""

import os
import requests
import time
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_image(prompt, filename, size="1792x1024", quality="standard", max_retries=3):
    """
    Generate an image using OpenAI DALL-E with retry logic
    
    Args:
        prompt (str): Description of the image to generate
        filename (str): Name for the saved file (include extension)
        size (str): Image size - "1024x1024", "1792x1024", or "1024x1792" 
        quality (str): "standard" or "hd"
        max_retries (int): Maximum number of retry attempts
    
    Returns:
        bool: True if successful, False otherwise
    """
    
    for attempt in range(max_retries):
        try:
            print(f"\n{'='*60}")
            print(f"GENERATING IMAGE {attempt + 1}/{max_retries}")
            print(f"File: {filename}")
            print(f"Size: {size} | Quality: {quality}")
            print(f"Prompt: {prompt}")
            print(f"{'='*60}")
            
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
            img_response = requests.get(image_url, timeout=30)
            if img_response.status_code == 200:
                # Ensure directory exists
                os.makedirs("static/images", exist_ok=True)
                
                filepath = f"static/images/{filename}"
                with open(filepath, "wb") as f:
                    f.write(img_response.content)
                
                # Verify file was saved and get size
                if os.path.exists(filepath):
                    file_size = os.path.getsize(filepath)
                    print(f"SUCCESS: Saved to {filepath}")
                    print(f"File size: {file_size:,} bytes")
                    return True
                else:
                    print(f"ERROR: File was not saved properly")
                    
            else:
                print(f"ERROR: Failed to download image (HTTP {img_response.status_code})")
                
        except Exception as e:
            print(f"ERROR (Attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in 3 seconds...")
                time.sleep(3)
    
    print(f"FAILED: Could not generate {filename} after {max_retries} attempts")
    return False

def generate_hero_backgrounds():
    """
    Generate all 4 hero background images for the Trilink website
    """
    
    # Color scheme from brand guidelines
    brand_colors = "navy blue #0B1F3B and teal #2AA198"
    common_requirements = f"Professional business aesthetic, {brand_colors} color scheme, very subtle and muted for text overlay, clean modern style"
    
    # Define all hero background specifications
    hero_images = [
        {
            "filename": "hero-accounting-subtle.jpg",
            "prompt": f"Abstract professional financial data visualization background, subtle charts and graphs, clean spreadsheet elements, {common_requirements}, minimal geometric patterns, suitable for accounting services webpage"
        },
        {
            "filename": "hero-automation-subtle.jpg", 
            "prompt": f"Subtle connected business systems background, abstract workflow visualization, clean technology patterns, connected nodes and pathways, {common_requirements}, minimal tech elements, suitable for business automation services"
        },
        {
            "filename": "hero-strategy-subtle.jpg",
            "prompt": f"Abstract business growth visualization, subtle upward trending elements, minimal arrow and growth patterns, {common_requirements}, strategic consulting aesthetic, clean geometric growth elements"
        },
        {
            "filename": "hero-contact-subtle.jpg",
            "prompt": f"Professional consultation office environment background, very subtle and muted, clean business setting with minimal office elements, {common_requirements}, consultation and meeting aesthetic"
        }
    ]
    
    print("TRILINK HERO BACKGROUND GENERATOR")
    print("=" * 60)
    print(f"Output directory: static/images/")
    print(f"Image size: 1792x1024 (landscape)")
    print(f"Quality: standard")
    print(f"Brand colors: {brand_colors}")
    print(f"Total images to generate: {len(hero_images)}")
    print("=" * 60)
    
    # Check API key
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found in environment variables")
        return False
        
    # Generate each image
    results = []
    successful = 0
    failed = 0
    
    start_time = time.time()
    
    for i, image_spec in enumerate(hero_images, 1):
        print(f"\nStarting generation {i}/{len(hero_images)}")
        
        success = generate_image(
            prompt=image_spec["prompt"],
            filename=image_spec["filename"],
            size="1792x1024",
            quality="standard"
        )
        
        results.append({
            "filename": image_spec["filename"],
            "success": success
        })
        
        if success:
            successful += 1
            print(f"COMPLETED: {image_spec['filename']}")
        else:
            failed += 1
            print(f"FAILED: {image_spec['filename']}")
            
        # Add delay between requests to be respectful to API
        if i < len(hero_images):
            print("Waiting 2 seconds before next generation...")
            time.sleep(2)
    
    # Final summary
    elapsed_time = time.time() - start_time
    print(f"\n{'='*60}")
    print("BATCH GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total time: {elapsed_time:.1f} seconds")
    print(f"Output location: static/images/")
    
    print(f"\nDETAILED RESULTS:")
    for result in results:
        status = "SUCCESS" if result["success"] else "FAILED"
        print(f"  {status}: {result['filename']}")
    
    if successful == len(hero_images):
        print(f"\nAll {len(hero_images)} hero background images generated successfully!")
        print("Ready to use in your Hugo templates.")
    elif successful > 0:
        print(f"\nPartially successful: {successful}/{len(hero_images)} images generated")
        print("You may want to retry the failed images.")
    else:
        print(f"\nGeneration failed completely. Check your API key and connection.")
    
    return successful == len(hero_images)

def main():
    """Main function to run batch generation"""
    try:
        success = generate_hero_backgrounds()
        return 0 if success else 1
    except KeyboardInterrupt:
        print(f"\nGeneration cancelled by user")
        return 1
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())