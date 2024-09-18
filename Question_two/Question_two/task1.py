from PIL import Image
# Generate the random number as described in the prompt
import time

current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print("generated Number:",generated_number)

# Open the image
img = Image.open("chapter1.jpg")
# Get the image size
width, height = img.size
# Create a new image with the same size
new_img = Image.new("RGB", (width, height))
#Iterate through each pixel and modify its RGB values
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        new_r = min(255, r + generated_number)  # Ensure values don't exceed 255
        new_g = min(255, g + generated_number)
        new_b = min(255, b + generated_number)
        new_img.putpixel((x, y), (new_r, new_g, new_b))

# Save the modified image
new_img.save("chapter1out.jpg")
print("new image is saved as chapter1out.jpg ")
# Calculate the sum of red pixel values
red_sum = 0
for x in range(width):
    for y in range(height):
        r, _, _ = img.getpixel((x, y))
        red_sum += r
print("Sum of red pixel values:", red_sum)
