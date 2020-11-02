
def ksiegi_decoding_key():

    letters= 'abcdefghijklmnoprstuwxyz'
    entered_element=[]
    returned_element=[]

    for letter in letters:
        entered_element.append(letter)
        returned_element.append(letters.index(letter)+11)

    decoding_dict=dict(zip(entered_element,returned_element))

    for num in range (0,10):
        decoding_dict[str(num)]=num

    return decoding_dict


def decoding(numer_ksiegi, decoder):

    numer_ksiegi=numer_ksiegi.replace(" ", "")
    numer_ksiegi=numer_ksiegi.replace("/", "")
    numer_ksiegi=numer_ksiegi.lower()

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

numer_ksiegiw=input("eneter the number: ")

print (decoding(numer_ksiegiw, ksiegi_decoding_key))
