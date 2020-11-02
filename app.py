
import string

#number_base = str(input("Wpisz postawę numeru księgi wieczystej: "))
def ksiegi_decoding_key():

    letters= string.ascii_lowercase
    entered_element=[]
    returned_element=[]

    for letter in letters:
        entered_element.append(letter)
        returned_elemen.append(letters.index(letter)+1)

    decoding_dict=dict(zip(entered_element,returned_elemen))

    for num in range (1,10):
        decoding_dict[str(num)]=num

    decoding_dict['/']=0

    return decoding_dict


def decoding(numer_ksiegi, decoder):

    decoded_elements = []

    for element in numer_ksiegi:
        decoded_elements.append(decoder()[element])

    total = []

    for num in decoded_elements[0::3]:
        total.append(num*1)

    for num in decoded_elements[1::3]:
        total.append(num*3)

    for num in decoded_elements[2::3]:
        total.append(num*7)

    return sum(total)%10
