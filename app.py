
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

ksiega_wieczysta = 'kr/1468/anna'
numerical = []

for element in ksiega_wieczysta:
    numerical.append(creating_decoder()[element])

total = []

for num in numerical[0::3]:
    total.append(num*1)

for num in numerical[1::3]:
    total.append(num*3)

for num in numerical[2::3]:
    total.append(num*7)

print (sum(total)%10)
