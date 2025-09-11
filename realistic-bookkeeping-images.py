#!/usr/bin/env python3
"""
Generate truly photorealistic, natural business images for bookkeeping services
Usage: python realistic-bookkeeping-images.py
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

def generate_image(prompt, filename, size="1024x1024", quality="standard", max_retries=3):
    """Generate an image using OpenAI DALL-E with retry logic"""
    
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

def generate_natural_bookkeeping_images():
    """Generate natural, photorealistic business images for bookkeeping services"""
    
    # Base requirements for natural business photography
    base_style = "Professional business photography, realistic lighting, authentic office environment, natural poses, high-quality corporate photography style"
    
    # Define all images with natural, authentic prompts
    images = [
        # Hero background - focus on the work environment
        {
            "filename": "hero-accounting-natural.jpg",
            "size": "1792x1024",
            "prompt": f"Professional accounting workspace with financial documents, calculator, and laptop showing spreadsheets on a modern office desk, natural office lighting from windows, clean organized workspace, {base_style}, realistic depth of field for text overlay"
        },
        
        # Service images - focus on authentic business scenarios
        {
            "filename": "account-setup-natural.jpg", 
            "size": "1024x1024",
            "prompt": f"Business professional reviewing financial documents and setting up accounting records at a modern office desk, natural business attire, {base_style}, authentic office consultation scene"
        },
        {
            "filename": "account-cleanup-natural.jpg",
            "size": "1024x1024", 
            "prompt": f"Organized desk with financial statements, receipts, and laptop showing accounting software being used for bookkeeping cleanup, {base_style}, realistic business workspace with papers being sorted"
        },
        {
            "filename": "software-training-natural.jpg",
            "size": "1024x1024",
            "prompt": f"Computer screen displaying QuickBooks accounting software interface with business professional working at desk, {base_style}, authentic software training environment in modern office"
        },
        {
            "filename": "payroll-natural.jpg",
            "size": "1024x1024",
            "prompt": f"Business desk with payroll documents, computer showing payroll software, and calculator, professional workspace for HR and payroll processing, {base_style}, realistic payroll management setup"
        },
        {
            "filename": "ongoing-bookkeeping-natural.jpg",
            "size": "1024x1024", 
            "prompt": f"Monthly financial reports and bank statements spread on office desk with laptop showing accounting dashboard, {base_style}, authentic monthly bookkeeping review workspace"
        },
        {
            "filename": "year-end-natural.jpg",
            "size": "1024x1024",
            "prompt": f"Tax preparation workspace with organized financial documents, 1099 forms, and laptop for year-end accounting work, {base_style}, realistic tax season preparation setup"
        }
    ]
    
    print("NATURAL BOOKKEEPING IMAGES GENERATOR")
    print("=" * 60)
    print(f"Output directory: static/images/")
    print(f"Style: Natural professional business photography")
    print(f"Focus: Authentic workspaces and business scenarios")
    print(f"Total images to generate: {len(images)}")
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
    
    for i, image_spec in enumerate(images, 1):
        print(f"\nStarting generation {i}/{len(images)}")
        
        success = generate_image(
            prompt=image_spec["prompt"],
            filename=image_spec["filename"],
            size=image_spec["size"],
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
        if i < len(images):
            print("Waiting 3 seconds before next generation...")
            time.sleep(3)
    
    # Final summary
    elapsed_time = time.time() - start_time
    print(f"\n{'='*60}")
    print("NATURAL BOOKKEEPING IMAGE GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total time: {elapsed_time:.1f} seconds")
    print(f"Output location: static/images/")
    
    print(f"\nDETAILED RESULTS:")
    for result in results:
        status = "SUCCESS" if result["success"] else "FAILED"
        print(f"  {status}: {result['filename']}")
    
    if successful == len(images):
        print(f"\nAll {len(images)} natural business images generated successfully!")
        print("Ready to update the bookkeeping page with new natural image references.")
    elif successful > 0:
        print(f"\nPartially successful: {successful}/{len(images)} images generated")
        print("You may want to retry the failed images.")
    else:
        print(f"\nGeneration failed completely. Check your API key and connection.")
    
    return successful == len(images)

if __name__ == "__main__":
    try:
        success = generate_natural_bookkeeping_images()
        exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\nGeneration cancelled by user")
        exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        exit(1)