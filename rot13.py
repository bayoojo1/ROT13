def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            offset = ord('a')
            result.append(chr(((ord(char) - offset + 13) % 26) + offset))
        elif 'A' <= char <= 'Z':
            offset = ord('A')
            result.append(chr(((ord(char) - offset + 13) % 26) + offset))
        else:
            result.append(char)
    return ''.join(result)

# Example usage:
input_text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"
encoded_text = rot13(input_text)
print("Encoded:", encoded_text)
