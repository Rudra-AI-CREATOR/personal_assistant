# Import the necessary libraries
from PIL import Image, ImageDraw, ImageFont

# Get the input text from the user
text = input("Enter the text you want to convert to an image: ")

# Set the font and font size
font = ImageFont.truetype("arial.ttf", 30)

# Set the image size
image_size = (800, 600)

# Create a new image with a white background
img = Image.new("RGB", image_size, (255, 255, 255))

# Create a drawing context
draw = ImageDraw.Draw(img)

# Draw the text on the image
draw.text((10, 10), text, font=font, fill=(0, 0, 0))

# Save the image to a file
img.save("text_image.png")