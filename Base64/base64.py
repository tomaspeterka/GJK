"""
import base64

decoded_file_name = "decoded_text.txt"
encoded_file_name = "encoded_text.txt"

with open(encoded_file_name, "r") as file:
    encoded_content = file.read()

encoded_content = encoded_content.encode("ascii")

decoding_base64 = base64.b64decode(encoded_content)
decoded_content = decoding_base64.decode("ascii")

with open(decoded_file_name, "w") as file:
    file.write(decoded_content)

print("Text has been decoded and saved to", decoded_file_name)

"""
import base64

encoded_file_name = "encoded_text.txt"
decoded_file_name = "decoded_text.txt"

with open(encoded_file_name, "r") as file:
    paragraphs = file.readlines()


decoded_paragraphs = []

for idx, paragraph in enumerate(paragraphs):
    decode_iterations = idx + 1  
    print(idx)
    if idx == 16:
        decode_iterations = 32

    encoded_content = paragraph.encode("ascii")

    for i in range(decode_iterations):
        decoding_base64 = base64.b64decode(encoded_content)
        encoded_content = decoding_base64

    decoded_content = decoding_base64.decode("ascii")
    decoded_paragraphs.append(decoded_content)

with open(decoded_file_name, "w") as file:
    for decoded_paragraph in decoded_paragraphs:
        file.write(decoded_paragraph + "\n")

print("Text has been decoded and saved to", decoded_file_name)
