def decrypt_caesar_cipher(text, shift):
    decrypted = []
    
    for char in text:
        if char.isalpha():
            shift_value = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_value - shift) % 26 + shift_value)
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)  # Keep non-alphabetic characters unchanged
    
    return ''.join(decrypted)

def find_correct_shift(ciphered_text):
    for shift in range(1, 26):
        decrypted_text = decrypt_caesar_cipher(ciphered_text, shift)
        print(f"Shift {shift}:")
        print(decrypted_text)
        print()

# Example ciphered text (you can change this with any cryptogram)
ciphered_text = """VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY
NAONG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"""

find_correct_shift(ciphered_text)
