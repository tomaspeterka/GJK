"""
import base64

with open("text.txt", "r") as file:
    content = file.read()
# print(file.read())

encoded_content = content.encode("ascii") 
  
decoding_base64 = base64.b64decode(encoded_content) 
decoded_file = decoding_base64.decode("ascii") 
  
print(f"Decoded string: {decoded_file}")  
"""


encoded_file_path = "text.txt"
output_file_path = "decoded_text.txt"


import base64

with open(encoded_file_path, "r") as encoded_file:

    with open(output_file_path, "w") as output_file:

        for line in encoded_file:
            decoded_line = base64.b64decode(line.encode("ascii")).decode("ascii")
            output_file.write(decoded_line)

print("File decoded and saved to", output_file_path)