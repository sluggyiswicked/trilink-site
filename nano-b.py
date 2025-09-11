import google.generativeai as genai

# Set up your API key (from Google AI Studio or Vertex AI)
genai.configure(api_key="AIzaSyDu64p-LDQ46tMPOmFcdGC8t3AmdhHd4q0")

print("Checking available image generation models and their supported methods...")

# List all models and check which ones support generation
image_models = []
all_models = list(genai.list_models())

for model in all_models:
    model_name_lower = model.name.lower()
    if any(keyword in model_name_lower for keyword in ['image', 'imagen', 'generate']):
        print(f"\n{model.name}: {model.display_name}")
        print(f"  Supported methods: {model.supported_generation_methods}")
        if 'generateContent' in model.supported_generation_methods:
            image_models.append(model.name)
            print(f"  [OK] Supports generateContent")
        else:
            print(f"  [NO] Does not support generateContent")

print(f"\nModels that support generateContent for images: {len(image_models)}")
for model_name in image_models:
    print(f"  - {model_name}")

# Test different prompting approaches for image generation
if image_models:
    for model_name in image_models:
        print(f"\n{'='*50}")
        print(f"Testing: {model_name}")
        
        try:
            test_model = genai.GenerativeModel(model_name)
            
            # Try different prompt styles
            prompts = [
                "Generate an image of a red circle",
                "Create a picture: red circle on white background", 
                "Image: simple red circle",
                "[IMAGE] red circle"
            ]
            
            for i, prompt in enumerate(prompts):
                print(f"\nPrompt {i+1}: '{prompt}'")
                try:
                    response = test_model.generate_content(prompt)
                    
                    # Check what we got back
                    has_text = False
                    has_image = False
                    
                    if hasattr(response, 'parts') and response.parts:
                        for j, part in enumerate(response.parts):
                            if hasattr(part, 'text') and part.text:
                                has_text = True
                                print(f"  Text response (truncated): {part.text[:100]}...")
                            elif hasattr(part, 'inline_data') and part.inline_data:
                                has_image = True
                                print(f"  Found image data in part {j}!")
                                import base64
                                filename = f"{model_name.split('/')[-1]}_prompt{i+1}_part{j}.png"
                                with open(filename, "wb") as f:
                                    f.write(base64.b64decode(part.inline_data.data))
                                print(f"  Saved as {filename}")
                    
                    if not has_text and not has_image:
                        print("  No text or image data found in response")
                        
                except Exception as e:
                    print(f"  Error with this prompt: {e}")
                    
        except Exception as e:
            print(f"Model failed entirely: {e}")
            if "quota" in str(e).lower():
                print("This appears to be a quota/billing issue")
                break
else:
    print("No image generation models found that support generateContent")
