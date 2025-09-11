#!/usr/bin/env python3
"""
Generate photorealistic images for the bookkeeping services page
Usage: python bookkeeping-images.py
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

def generate_bookkeeping_images():
    """Generate all images needed for the bookkeeping services page"""
    
    # Common photorealistic requirements
    common_style = "Photorealistic professional business photography, warm natural lighting, high-end corporate environment, depth of field with background blur for text overlay, authentic business atmosphere"
    
    # Define all images needed for bookkeeping page
    images = [
        # Hero background
        {
            "filename": "hero-accounting-realistic.jpg",
            "size": "1792x1024",
            "prompt": f"Photorealistic accounting office scene with professional accountant working at modern desk with financial documents, calculator, and computer showing spreadsheets, warm office lighting, depth of field with background blur for text overlay, {common_style}, authentic accounting workspace environment"
        },
        
        # Service card images (1024x1024)
        {
            "filename": "account-setup-realistic.jpg", 
            "size": "1024x1024",
            "prompt": f"Photorealistic business consultation scene with accountant helping client set up new business accounts, reviewing paperwork and charts of accounts on modern office desk, {common_style}, professional account setup consultation"
        },
        {
            "filename": "account-cleanup-realistic.jpg",
            "size": "1024x1024", 
            "prompt": f"Photorealistic accounting workspace with stacks of financial documents being organized and reconciled, computer screen showing accounting software, calculator and pen on desk, {common_style}, account cleanup and catch-up work environment"
        },
        {
            "filename": "software-training-realistic.jpg",
            "size": "1024x1024",
            "prompt": f"Photorealistic office training session with instructor teaching QuickBooks software on computer screen to business professionals, modern conference room setting, {common_style}, accounting software training environment"  
        },
        {
            "filename": "payroll-realistic.jpg",
            "size": "1024x1024",
            "prompt": f"Photorealistic payroll processing scene with HR professional working on computer showing payroll software interface, employee timesheets and tax forms on desk, {common_style}, authentic payroll management workspace"
        },
        {
            "filename": "ongoing-bookkeeping-realistic.jpg",
            "size": "1024x1024", 
            "prompt": f"Photorealistic monthly bookkeeping scene with accountant reviewing financial reports and bank statements at organized desk, computer showing accounting dashboard, {common_style}, ongoing bookkeeping and monthly close environment"
        },
        {
            "filename": "year-end-realistic.jpg",
            "size": "1024x1024",
            "prompt": f"Photorealistic year-end accounting preparation with accountant preparing tax documents and adjusting entries, desk with organized financial records and laptop, {common_style}, year-end tax preparation workspace"
        }
    ]
    
    print("BOOKKEEPING PAGE IMAGE GENERATOR")
    print("=" * 60)
    print(f"Output directory: static/images/")
    print(f"Style: Photorealistic business photography with warm natural lighting")
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
    print("BOOKKEEPING IMAGE GENERATION COMPLETE")
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
        print(f"\nAll {len(images)} bookkeeping images generated successfully!")
        print("Ready to update the bookkeeping page with new image references.")
    elif successful > 0:
        print(f"\nPartially successful: {successful}/{len(images)} images generated")
        print("You may want to retry the failed images.")
    else:
        print(f"\nGeneration failed completely. Check your API key and connection.")
    
    return successful == len(images)

if __name__ == "__main__":
    try:
        success = generate_bookkeeping_images()
        exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\nGeneration cancelled by user")
        exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        exit(1)