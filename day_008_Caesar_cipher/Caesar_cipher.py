# Caesar cipher is a cipher method with letter shift
# Program will ask us if we want to decode or encode the cipher
# If we select encode it will ask as for the words and the shift then it will encode over message
# If we select decode it will ask as for the words and the shift then it will decode the message

from letters import letters
from art import logo

def try_shift():
    while True:
        try:
            shift_try = int(input("enter shift: "))
            return shift_try
        except ValueError:
            print("Wrong input")

def what_to_do():
    while True:
        output= input('Would you like to "decode" or "encode" the message: ').lower()
        if output == "encode" or output == "decode":
            return output
        else:
            print("wrong input")

# def encode(message,shift):
#     encoded_message = []
#     for letter in range(len(message)):
#         if not message[letter].isalpha():
#             encoded_message.append(message[letter])
#         else:
#             letter_index = letters.index(message[letter])
#             encoded_message.append((letters[(letter_index + shift)%26]))
#     print(''.join(encoded_message))
#
#
# def decode(message, shift):
#     decoded_message = []
#     for letter in range(len(message)):
#         if not message[letter].isalpha():
#             decoded_message.append(message[letter])
#         else:
#             letter_index = letters.index(message[letter])
#             decoded_message.append((letters[(letter_index - shift)%26]))
#     print(''.join(decoded_message))

def cesar(message, shift, encode_or_decode):
    output_message = []
    if encode_or_decode == "decode":
        shift *= -1

    for letter in range(len(message)):
        if not message[letter].isalpha():
            output_message.append(message[letter])
        else:
            letter_index = letters.index(message[letter])
            output_message.append((letters[(letter_index + shift) % 26]))
    print(f"This is your {encode_or_decode}d message: "+''.join(output_message))


i = "yes"
print(logo)
while i == "yes":
    print("We are going to encode your message or decode message that you have received")
    decode_or_encode = what_to_do()
    message_to_change = input("enter message: ").lower()
    shift_to_change = try_shift()
    cesar(message_to_change, shift_to_change, decode_or_encode)
    i =input("type \"yes\" if you wold like to do if not type \"no\": ").lower()

