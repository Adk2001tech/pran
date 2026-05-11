import os
from PIL import Image, ImageDraw

def create_gradient(width, height, color1, color2):
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def main():
    os.makedirs('static/images', exist_ok=True)
    
    # Soft pastel color pairs
    palettes = [
        ((255, 218, 224), (240, 230, 240)), # Blush pink to lavender
        ((224, 255, 255), (255, 224, 255)), # Light cyan to pink
        ((255, 239, 213), (255, 228, 225)), # Papaya whip to misty rose
        ((230, 230, 250), (255, 240, 245)), # Lavender to lavender blush
        ((240, 255, 240), (245, 245, 220)), # Honeydew to beige
        ((255, 245, 238), (255, 228, 196)), # Seashell to bisque
        ((240, 248, 255), (230, 230, 250)), # Alice blue to lavender
        ((255, 250, 240), (255, 240, 245)), # Floral white to lavender blush
        ((245, 255, 250), (240, 255, 255)), # Mint cream to azure
        ((255, 228, 225), (255, 218, 185)), # Misty rose to peach puff
    ]

    for i, (c1, c2) in enumerate(palettes):
        img = create_gradient(1920, 1080, c1, c2)
        filename = f'static/images/page{i+1}.png'
        img.save(filename)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
