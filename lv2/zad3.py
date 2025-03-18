import numpy as np
import matplotlib.pyplot as plt

# Učitavanje slike
tiger_img = plt.imread("tiger.png")
if tiger_img.dtype == np.uint8:
    tiger_img = tiger_img.astype(np.float32) / 255.0

def increase_brightness(image, value=0.2): 
    bright_img = np.clip(image + value, 0, 1)
    return bright_img   # Povecana svjetlina

def rotate_image(image):
    return np.rot90(image, k=-1)  # Rotacija 90 stupnjeva u smjeru kazaljke na satu

def mirror_image(image):
    return np.fliplr(image)  # Zrcaljenje slike

def downscale_image(image, factor=10): 
    new_size = (image.shape[0] // factor, image.shape[1] // factor, image.shape[2])
    return image[::factor, ::factor, :]  # Smanjena rezolucija

def extract_second_quarter(image): 
    black_image = np.zeros_like(image)
    height, width = image.shape[:2]
    start_col = width // 4
    end_col = width // 2
    black_image[:, start_col:end_col] = image[:, start_col:end_col]
    return black_image  # Zadnja cetvrtina

bright_img = increase_brightness(tiger_img, 0.2)
rotated_img = rotate_image(tiger_img)
mirrored_img = mirror_image(tiger_img)
downscaled_img = downscale_image(tiger_img, 10)
second_quarter_img = extract_second_quarter(tiger_img)

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs = axs.ravel()

titles = ["Originalna slika", "Posvijetljena slika", "Rotirana slika", "Zrcaljena slika", "Smanjena rezolucija", "Druga četvrtina"]
images = [tiger_img, bright_img, rotated_img, mirrored_img, downscaled_img, second_quarter_img]

for i in range(6):
    axs[i].imshow(images[i])
    axs[i].set_title(titles[i])
    axs[i].axis("off")

plt.tight_layout()
plt.show()