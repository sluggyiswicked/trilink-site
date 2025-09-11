import google.generativeai as genai
import base64
from PIL import Image
from io import BytesIO

# Set up your API key 
genai.configure(api_key="AIzaSyDu64p-LDQ46tMPOmFcdGC8t3AmdhHd4q0")

print("Testing Google image generation with correct API pattern...")

# Use the correct model and approach
try:
    model = genai.GenerativeModel("gemini-2.5-flash-image-preview")
    prompt = "Create a simple red circle on a white background, digital art style, clean and minimalist"
    
    print("Generating image...")
    response = model.generate_content(prompt)
    
    print(f"Response received!")
    print(f"Response type: {type(response)}")
    print(f"Has candidates: {hasattr(response, 'candidates')}")
    
    if hasattr(response, 'candidates') and response.candidates:
        print(f"Number of candidates: {len(response.candidates)}")
        for i, candidate in enumerate(response.candidates):
            print(f"Candidate {i}:")
            print(f"  Has content: {hasattr(candidate, 'content')}")
            if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                print(f"  Number of parts: {len(candidate.content.parts)}")
                for j, part in enumerate(candidate.content.parts):
                    print(f"  Part {j} type: {type(part)}")
                    if hasattr(part, 'text'):
                        print(f"    Text: {part.text[:100]}...")
                    if hasattr(part, 'inline_data') and part.inline_data:
                        print(f"    Found image data! MIME type: {part.inline_data.mime_type}")
                        filename = f"google_circle_{i}_{j}.png"
                        with open(filename, "wb") as f:
                            f.write(base64.b64decode(part.inline_data.data))
                        print(f"    Image saved as {filename}")
                        
                        import os
                        size = os.path.getsize(filename)
                        print(f"    File size: {size} bytes")
    else:
        print("No candidates found in response")
        # Try alternate response structure
        if hasattr(response, 'parts'):
            print(f"Response has parts: {len(response.parts)}")
            for i, part in enumerate(response.parts):
                print(f"Part {i}: {type(part)}")
                if hasattr(part, 'inline_data'):
                    print(f"Found image in direct parts!")

except Exception as e:
    print(f"Failed: {e}")
    if "quota" in str(e).lower() or "billing" in str(e).lower():
        print("\nThis appears to be a quota/billing issue.")
        print("Solutions:")
        print("1. Wait for quota reset (daily/hourly limits)")  
        print("2. Enable billing in Google AI Studio")
        print("3. Upgrade to paid tier")
        print("4. Try again later")
    else:
        print("This might be an API configuration issue.")