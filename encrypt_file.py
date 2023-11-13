
from PIL import Image
import stepic

image_path = input("Enter img Name: ")

data_to_encode = input("Enter data to encode: ")
original_image = Image.open(image_path)
encoded_image = stepic.encode(original_image, data_to_encode.encode())
encoded_image.save('new.png', 'PNG')