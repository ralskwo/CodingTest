alphabet_string = input().strip()

converted_numbers = [str(ord(char) - ord('A') + 1) for char in alphabet_string]

print(" ".join(converted_numbers))