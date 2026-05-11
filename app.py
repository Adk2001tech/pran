import json
import random
import os
from flask import Flask, render_template

app = Flask(__name__)

def load_quotes():
    """Loads quotes from the JSON data file."""
    with open('data/quotes.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    """Renders the main page with a random quote and image."""
    quotes = load_quotes()
    random_quote = random.choice(quotes)
    
    # Get list of floating images
    floating_dir = 'static/images/floating'
    floating_images = []
    if os.path.exists(floating_dir):
        # Support common image extensions
        extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg')
        floating_images = [f for f in os.listdir(floating_dir) if f.lower().endswith(extensions)]
    
    return render_template('index.html', quote=random_quote, floating_images=floating_images)

if __name__ == '__main__':
    # Using 0.0.0.0 to make it accessible if needed, default port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
