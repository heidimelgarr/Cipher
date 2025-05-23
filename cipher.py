"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Heidi Melgar, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: he3839
"""


# TO DO implement this function. You may delete this comment after you are done.
def rail_fence_encode(string, key):
    """
    pre: string is a string of characters and key is a positive
        integer 2 or greater and strictly less than the length
        of string
    post: returns a single string that is encoded with
        rail fence algorithm
    """
    if key == 1:
        return string # no encoding

    # list of rails
    rails = ['' for _ in range(key)]
    step = 1
    row = 0

    for char in string:
        rails[row] += char
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step
    return ''.join(rails)


# TO DO
def rail_fence_decode(string, key):
    """
    pre: string is a string of characters and key is a positive
        integer 2 or greater and strictly less than the length
        of string
    post: function returns a single string that is decoded with
        rail fence algorithm
    """
    if key == 1 or key == len(string):
        return string

    pattern = [None] * len(string)
    direction = 1
    curr_rail = 0

    # zigzag pattern
    for i in range(len(string)):
        pattern[i] = curr_rail
        if curr_rail in {0, key - 1}:
            direction = -direction
        curr_rail += direction

    rails = ['' for _ in range(key)]

    # fill rails
    i = 0
    for r in range(key):
        for c in range(len(string)):
            if pattern[c] == r:
                rails[r] += string[i]
                i += 1

    # decoded message in pattern
    decoded = ''
    rail_point = [0] * key
    for c in range(len(string)):
        rail = pattern[c]
        if rail_point[rail] < len(rails[rail]):
            decoded += rails[rail][rail_point[rail]]
            rail_point[rail] += 1
    return decoded


# TO DO
def filter_string(string):
    """
    pre: string is a string of characters
    post: function converts all characters to lower case and then
        removes all digits, punctuation marks, and spaces. It
        returns a single string with only lower case characters
    """
    filter_char = []
    for char in string:
        if char.isalpha():
            filter_char.append(char.lower())
    return ''.join(filter_char)


# TO DO
def encode_character(p, s):
    """
    pre: p is a character in the pass phrase and s is a character
        in the plain text
    post: function returns a single character encoded using the
        Vigenere algorithm. You may not use a 2-D list
    """
    # Convert characters
    p_char = ord(p) - ord('a')
    s_char = ord(s) - ord('a')

    # Use modulo to wrap around
    encoded_val = (s_char + p_char) % 26

    # Convert back to a char
    return chr(encoded_val + ord('a'))


# TO DO
def decode_character(p, s):
    """
    pre: p is a character in the pass phrase and s is a character
        in the encrypted text
    post: function returns a single character decoded using the
        Vigenere algorithm. You may not use a 2-D list
    """
    # Convert characters
    p_char = ord(p) - ord('a')
    s_char = ord(s) - ord('a')

    # Use modulo to wrap around
    decoded_char = (s_char - p_char) % 26

    # Convert back to a character and return
    return chr(decoded_char + ord('a'))


# TO DO
def vigenere_encode(string, phrase):
    """
    pre: string is a string of characters and phrase is a pass phrase
    post: function returns a single string that is encoded with
        Vigenere algorithm
    """
    filtered_str = filter_string(string)  # Filter out non alphabet
    filtered_phrase = filter_string(phrase)  # Filter the passphrase

    encoded_text = ""
    phrase_index = 0

    # Encode each char
    for char in filtered_str:
        phrase_char = filtered_phrase[phrase_index % len(filtered_phrase)]
        encoded_char = encode_character(phrase_char, char)  # Encode the character
        encoded_text += encoded_char  # Append to the result
        phrase_index += 1

    return encoded_text


# TO DO
def vigenere_decode(string, phrase):
    """
    pre: string is a string of characters and phrase is a pass phrase
    post: function returns a single string that is decoded with
        Vigenere algorithm
    """
    filtered_str = filter_string(string)  # Filter out non-alphabet
    filtered_phrase = filter_string(phrase)

    decoded_text = ""
    phrase_index = 0

    # Decode each char
    for char in filtered_str:
        phrase_char = filtered_phrase[phrase_index % len(filtered_phrase)]
        decoded_char = decode_character(phrase_char, char)  # Decode the character
        decoded_text += decoded_char
        phrase_index += 1

    return decoded_text


# TO DO
def main():
    """Main function that reads stdin and runs each cipher"""
     # read the plain text from stdin (terminal/input)
    pt_rf = input("Plain text: ").strip()
    # read the key from stdin (terminal/input)
    k_rf = int(input("Key: ").strip())

    # encrypt and print the encoded text using rail fence cipher
    enc_rf = rail_fence_encode(pt_rf, k_rf)
    print(f"Encoded (Rail Fence): {enc_rf}")

    # read encoded text from stdin (terminal/input)
    enc_rf_input = input("Encoded (decrypt): ").strip()
    # read the key from stdin (terminal/input)
    k_rf_input = int(input("Key (decrypt): ").strip())

    # decrypt and print the plain text using rail fence cipher
    dec_rf = rail_fence_decode(enc_rf_input, k_rf_input)
    print(f"Decoded Rail Fence): {dec_rf}")

    # read the plain text from stdin (terminal/input)
    pt_vig = input("Plain text: ").strip()
    # read the pass phrase from stdin (terminal/input)
    pass_vig = input("Passphrase: ").strip()

    # encrypt and print the encoded text using Vigenere cipher
    enc_vig = vigenere_encode(pt_vig, pass_vig)
    print(f"Encoded Vigenere): {enc_vig}")

    # read the encoded text from stdin (terminal/input)
    enc_vig_input = input("Encoded (decrypt): ").strip()
    # read the pass phrase from stdin (terminal/input)
    pass_vig_input = input("Passphrase (decrypt): ").strip()

    # decrypt and print the plain text using Vigenere cipher
    dec_vig = vigenere_decode(enc_vig_input, pass_vig_input)
    print(f"Decoded (Vigenere): {dec_vig}")

# Do NOT modify the following code.
if __name__ == "__main__":
    main()
