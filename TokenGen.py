import random
import string
tokenlength = 59
chars = string.ascii_letters + string.digits
print("Hi welcome to the Discord Token Generator!")
Ntoken = int(input("How many tokens do you want to generate?: "))

tokens = []

for i in range(Ntoken):
    token = ""
    for i in range(tokenlength):
        token += random.choice(chars)
    tokens.append(token)
    print(token)

print("Tokens have been generated!")
print("Thank you for using the Discord Token Generator!")

# Save tokens to a file
filename = "tokens.txt"
with open(filename, "w") as file:
    file.write("\n".join(tokens))

print(f"Tokens have been saved to {filename}!")
