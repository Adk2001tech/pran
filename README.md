# Random Cute Quote Website ✨

A simple, aesthetic web application that displays a random cute quote and a beautiful background image every time the page is loaded or refreshed.

## Features
- **Randomized Experience:** Automatically picks a new quote and background on every refresh.
- **Aesthetic UI:** Pinterest/Tumblr inspired design with soft colors, elegant fonts, and rounded edges.
- **Smooth Animations:** Subtle background zoom and content fade-in.
- **Responsive:** Works beautifully on mobile, tablet, and desktop.
- **Fast & Lightweight:** Built with Flask and Vanilla CSS/JS.

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3 (Vanilla), JavaScript
- **Fonts:** Dancing Script, Poppins, Quicksand (Google Fonts)
- **Assets:** Locally generated aesthetic gradients.

## Setup Instructions

### 1. Install Dependencies
Ensure you have Python installed, then run:
```bash
python3 -m pip install -r requirements.txt
```

### 2. Generate Placeholder Assets
To initialize the aesthetic background images, run the setup script:
```bash
python3 setup_images.py
```

### 3. Run the Application
Start the Flask server:
```bash
python3 app.py
```

Open your browser and navigate to `http://localhost:5000`.

## Project Structure
- `app.py`: Main Flask application.
- `data/quotes.json`: Data store for quotes and image mappings.
- `static/css/style.css`: All aesthetic styling and animations.
- `static/images/`: Background image assets.
- `templates/index.html`: Main frontend template.
- `setup_images.py`: Utility script to generate local placeholder assets.

## Future Ideas (V2)
- Music toggle for soft lo-fi beats.
- "Favorite" button to save quotes locally.
- Share button for social media.
- Dark mode support.
