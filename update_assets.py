import os
import requests
import random

def download_backgrounds():
    print("Downloading aesthetic backgrounds...")
    os.makedirs('static/images', exist_ok=True)
    
    # Unsplash source terms for aesthetic/cute backgrounds
    terms = ["aesthetic-pastel", "cozy-room", "soft-nature", "feminine-aesthetic", "aesthetic-flower"]
    
    for i in range(1, 11):
        term = random.choice(terms)
        # Using a reliable Unsplash random URL
        url = f"https://images.unsplash.com/photo-{random.randint(1000000000000, 2000000000000)}?auto=format&fit=crop&w=1920&q=80"
        # Since I can't guess valid photo IDs easily, I'll use the source/random redirect if it still works or a few known good ones.
        # Actually, let's use a simpler approach: a set of 10 known high-quality aesthetic IDs.
        ids = [
            "1518117601-2100bb67a93b", # Pastel clouds
            "1501747315-124a0bca360f", # Soft flowers
            "1497215728101-856f4ea42174", # Minimal plant
            "1490730141103-6ca21aa62c48", # Sunset aesthetic
            "1528459801416-a7e9e2846506", # Pink texture
            "1557683316-973673baf926", # Abstract pastel
            "1464822759023-fed622ff2c3b", # Misty mountains
            "1519751138087-5bf79df62d5b", # Glitter/Bokeh
            "1516533075015-ba397384af96", # Minimalist cozy
            "1470770841072-f978cf4d019e"  # Serene nature
        ]
        
        img_id = ids[i-1]
        url = f"https://images.unsplash.com/photo-{img_id}?auto=format&fit=crop&w=1920&q=80"
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(f'static/images/page{i}.png', 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded background {i}/10")
            else:
                print(f"Failed to download background {i}")
        except Exception as e:
            print(f"Error downloading background {i}: {e}")

def create_placeholder_emojis():
    print("Creating placeholder floating elements...")
    os.makedirs('static/images/floating', exist_ok=True)
    
    # We'll create simple text-based icons for now so the system works
    # User will replace these with actual PNGs later
    emojis = {
        "sunflower.png": "🌻",
        "rasgulla.png": "⚪", # Placeholder
        "dark_fantasy.png": "🍫",
        "mumbai_pune_mumbai.png": "🎬"
    }
    
    # In a real scenario, we'd want actual PNGs. For this environment,
    # I'll just create empty files if I can't generate images easily, 
    # but the user wants to add them. I'll provide a few actual emojis as text for now in the UI.
    for filename in emojis.keys():
        path = os.path.join('static/images/floating', filename)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write("") # Create empty file as placeholder
            print(f"Created placeholder for {filename}")

if __name__ == "__main__":
    download_backgrounds()
    create_placeholder_emojis()
