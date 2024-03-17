# Chiffre mit shift/versatz im Alphabet
# encode & decode function
# 65 bis 126

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

text_list = list(text)

def encrypt(text_list, shift):
    for i in range(0, len(text_list)): 
        if text_list[i] in alphabet:
            index_alphabet = alphabet.index(text_list[i])
            new_index = (index_alphabet + shift)%26
            text_list[i] = alphabet[new_index]
    text_list = "".join(text_list)
    return text_list 

encrypted_text = encrypt(text_list, shift)
        
print(f"Your encrypted text is: {encrypted_text}")


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.