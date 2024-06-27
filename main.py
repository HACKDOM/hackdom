from dictionary import *
run_system = True
def encode(blank_text,message_input):
    for a in message_input:
        blank_text += alphanum[a]
    return blank_text
def decode(message_input):
    number_of_sequence = 0
    five_binary_combination = ""
    numalpha_sequence = ""
    for b in message_input:
        if number_of_sequence < 5:
            five_binary_combination += b
            if number_of_sequence == 4:
                numalpha_sequence += numalpha[five_binary_combination]
            number_of_sequence += 1
            if number_of_sequence == 5:
                number_of_sequence = 0
                five_binary_combination = ""
    output = str(numalpha_sequence).capitalize()
    return output
while run_system == True:
    decode_encode = input("Encode or Decode ? ").lower()
    # message = input("Please Type A Message?\n").upper()
    f = open("encoded_message.txt", "r")
    message = f.read().upper()
    blank = ""
    if decode_encode == "encode":
        encoded_result = encode(blank,message)
        with open('decoded_message.txt', 'w') as output_file:
            output_file.write(encoded_result)
        # print("You're Encoded Result Is Here : " ,encoded_result)
    elif decode_encode == "decode":
        f = open("decoded_message.txt", "r")
        kt = f.read()
        decoded_result = decode(kt)
        print("You're Decoded Result Is Here : " ,decoded_result)
    run_again = input("Do You Want to Run Again? yes or no").lower()
    if run_again == "yes":
        run_system = True
    else:
        run_system = False