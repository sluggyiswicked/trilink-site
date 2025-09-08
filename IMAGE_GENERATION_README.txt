TRILINK COLLABORATIVE - IMAGE GENERATION UTILITIES
=================================================

This project includes two Python scripts for generating images using OpenAI's DALL-E 3:

1. INTERACTIVE GENERATOR (image_generator.py)
   - Interactive script for one-off image generation
   - Prompts user for prompt, filename, size, and quality
   - Usage: python image_generator.py

2. BATCH GENERATOR (simple_batch_generator.py)
   - Non-interactive batch generation script
   - Generates all 4 hero background images automatically
   - Usage: python simple_batch_generator.py

REQUIREMENTS:
- OpenAI API key in .env file (OPENAI_API_KEY)
- Python packages: openai, requests, python-dotenv
- Internet connection

GENERATED HERO BACKGROUNDS (1792x1024, standard quality):
- hero-accounting-subtle.jpg (3.3MB) - Financial data visualization
- hero-automation-subtle.jpg (3.1MB) - Business systems workflow  
- hero-strategy-subtle.jpg (1.7MB) - Business growth visualization
- hero-contact-subtle.jpg (2.2MB) - Professional office environment

BRAND COLORS USED:
- Navy blue: #0B1F3B
- Teal: #2AA198

All images are optimized for text overlay with subtle, muted backgrounds
that complement the site's professional business aesthetic.

OUTPUT LOCATION: static/images/

GENERATION COST: ~$0.04 per image (standard quality, 1792x1024)