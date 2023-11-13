from PIL import Image
import stepic

def decode_data(encoded_image):
    data = stepic.decode(encoded_image)
    print("Decoded data: " + str(data))


encoded_image_path = input("Enter img Name: ")
encoded_image = Image.open(encoded_image_path)
decode_data(encoded_image)