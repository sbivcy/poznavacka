import os
from PIL import Image
from random import choice, sample

# Vytvořit seznam s obsahem složky images/
images = os.listdir("images/")

# Vytvořit seznam obrázků na test
if input("Povolit opakování? (y/N) ").lower() == "y":
    images = [choice(images) for _ in range(0, int(input("počet: ")))] 
else:
    images = sample(images, int(input(f"počet(1-{len(images)}): "))))

# Inicializace počítadla správných odpovědí
correct = 0

# Projít všechny obrázky v seznamu
for image in images:
    # Ukázat obrázek
    Image.open(f"images/{image}").show()
    if input("Odpověď: ").lower() == image[:-4].lower():
        print("Správně")
        correct += 1
    else:
        print(f"Správná odpověď: {image[:-4]}")

print(f"({correct}/{len(images)})")
