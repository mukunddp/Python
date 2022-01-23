'''import base64

with open("xyz.PNG", "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())
    print(b64_string.decode('utf-8'))'''

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)