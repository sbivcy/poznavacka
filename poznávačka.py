import os
from PIL import Image
from random import choice, sample

images = os.listdir("images/")
if input("Povolit opakování? (y/N) ").lower() == "y":
    images = [choice(images) for _ in range(0, int(input("počet: ")))] 
else:
    images = sample(images, len(images))

correct = 0
for image in images:
    Image.open(f"images/{image}").show()
    if input("Odpověď: ").lower() == image[:-4].lower():
        print("Správně")
        correct += 1
    else:
        print(f"Správná odpověď: {image[:-4]}")

print(f"({correct}/{len(images)})")
