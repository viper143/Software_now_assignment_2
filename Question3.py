#the encrypted text is saved as encrypted_code.txt
#decrypted code is saved as decryted_code.txt
total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2

print("Counter:", counter)
print("Total:", total)

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text
# decrypting function: Taking the reference on the function of encrption
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Read the encrypted text from a file
with open("encrypted_code.txt", "r") as file:
    encrypted_code = file.read()

# Key value for decryption (you can set it based on the value you used for encryption)
key = total # Example key, you can change this

# Decrypt the text
decrypted_code = decrypt(encrypted_code, key)

# Save the decrypted text to a new file
with open("OriginalDecryptedCode.txt", "w") as output_file:
    output_file.write(decrypted_code)

print("Decryption complete. Decrypted code saved in 'OriginalDecryptedCode.txt'.")
