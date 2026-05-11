console.log("%c ✨ Stay magical! ✨ ", "color: #ffb6c1; font-size: 20px; font-weight: bold;");

document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('floating-container');
    
    // Fallback emojis for when PNGs are missing
    const fallbacks = {
        'sunflower.png': '🌻',
        'rasgulla.png': '⚪',
        'dark_fantasy.png': '🍫',
        'mumbai_pune_mumbai.png': '🎬'
    };

    // Function to create a floating item
    function createFloatingItem(imgName) {
        const item = document.createElement('div');
        item.className = 'floating-item';
        
        // Random position
        item.style.left = Math.random() * 90 + 'vw';
        item.style.top = Math.random() * 90 + 'vh';
        
        // Random animation delay and duration
        item.style.animationDelay = Math.random() * -15 + 's';
        item.style.animationDuration = (15 + Math.random() * 15) + 's';
        
        // Random size variation
        const size = 60 + Math.random() * 60;
        item.style.width = size + 'px';
        item.style.height = size + 'px';

        const img = document.createElement('img');
        img.src = staticBase + imgName;
        img.alt = imgName;
        img.style.borderRadius = '50%'; // Make them look circular/emoji-like if they are images
        
        img.onload = () => {
            // Check if it's an empty/placeholder file (0 width)
            if (img.naturalWidth > 0) {
                item.appendChild(img);
            } else {
                item.textContent = fallbacks[imgName] || '✨';
            }
        };
        
        img.onerror = () => {
            // If it's not in our fallback list, show a random cute emoji
            const randomCute = ['✨', '💖', '🌸', '☁️', '🧚', '🌻', '🍭'];
            item.textContent = fallbacks[imgName] || randomCute[Math.floor(Math.random() * randomCute.length)];
        };
        
        container.appendChild(item);
    }

    // Spawn 5 items
    for (let i = 0; i < 5; i++) {
        const randomImg = floatingImages[Math.floor(Math.random() * floatingImages.length)];
        if (randomImg) {
            createFloatingItem(randomImg);
        } else {
            // If no images in folder, spawn random generic emojis
            const generic = ['✨', '💖', '🌸', '☁️', '🧚'];
            const item = document.createElement('div');
            item.className = 'floating-item';
            item.style.left = Math.random() * 90 + 'vw';
            item.style.top = Math.random() * 90 + 'vh';
            item.textContent = generic[Math.floor(Math.random() * generic.length)];
            container.appendChild(item);
        }
    }
});
