
import string

#number_base = str(input("Wpisz postawę numeru księgi wieczystej: "))
def creating_decoder():
    letters= string.ascii_lowercase
    key=[]
    value=[]

    for letter in letters:
        key.append(letter)
        value.append(letters.index(letter)+1)

    decoding_dict=dict(zip(key,value))

    for num in range (1,10):
        decoding_dict[str(num)]=num

    decoding_dict['/']=0

    return decoding_dict
