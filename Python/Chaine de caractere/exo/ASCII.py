def encode_ascii():
    return [chr(i) for i in range(128)]

encoded_ascii = encode_ascii()

combined_string = "".join(encoded_ascii)

print(combined_string)