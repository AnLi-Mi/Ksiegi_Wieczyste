from flask import Flask, render_template, request
import sady


app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    numer_ksiegiw = ''
    sad = ''
    error=''
    kode = ''
    edited_number = ''
    if request.method=="POST" and 'numer_ksiegiw' in request.form:
        numer_ksiegiw = request.form.get('numer_ksiegiw')
        kode = court_kode(numer_ksiegiw)
        edited_number=numer_ksiegiw.replace(" ", "")
        edited_number=edited_number.replace("/", "")
        if kode in sady.list_kod and len(edited_number)<= 12 :
            result = decoding(numer_ksiegiw, encoding_key_for_kw)
            sad = find_court(numer_ksiegiw)
        else:
            error= "Błędny numer"
    return render_template("index.html", kode=kode, edited_number=edited_number, error = error, result = result, sad = sad, numer_ksiegiw=numer_ksiegiw)

# creating the dictionary with letters and digits as keys and thier encoding result as values
def encoding_key_for_kw():

    #preparing lists of elemets before and after encoding
    #in order to turn them into a dictionary by zipping later
    entered_element=[]
    returned_element=[]

    # each letter's result after encoding is it's position in aphabet +10
    # (staring from 1, not 0)
    for letter in 'abcdefghijklmnoprstuwxyz':
        entered_element.append(letter)
        returned_element.append('abcdefghijklmnoprstuwxyz'.index(letter)+11)

    # zipping both lists to create a dictionary of a letter as a key
    # and it's numerical representation after encoding as a value
    decoding_dict=dict(zip(entered_element,returned_element))

    # adding the digits (as string) and their numerical representation
    # after encoding (the same digit) to the distionary
    for num in range (0,10):
        decoding_dict[str(num)]=num

    #returning complete dictionary
    return decoding_dict

# generating a last number of the Księga Wieczysta based on inputed base string
def decoding(numer_ksiegi, decoder):
    # editing users input so it's we can perform further operations on it
    numer_ksiegi=numer_ksiegi.replace(" ", "")
    numer_ksiegi=numer_ksiegi.replace("/", "")
    numer_ksiegi=numer_ksiegi.lower()
    zeros = (12-len(numer_ksiegi))*"0"
    numer_ksiegi=numer_ksiegi[:4] + zeros + numer_ksiegi[4:]
    

     

    # encoding the entered string using the encoding_key_for_kw()
    decoded_elements = []
    for element in numer_ksiegi:
        decoded_elements.append(decoder()[element])

    #preparing a list for decoded_elements after specific muliplications
    total = []

    # every third element starting from the first one is multipled by 1
    for num in decoded_elements[0::3]:
        total.append(num*1)

    # every third element starting from the second one is multipled by 3
    for num in decoded_elements[1::3]:
        total.append(num*3)

    # every third element starting from the third one is multipled by 7
    for num in decoded_elements[2::3]:
        total.append(num*7)

    # return the rest from dividing by 10 the sum of all numbers
    # after specific multiplications
    return numer_ksiegi


def court_kode(num_ksiegi):
    kode=num_ksiegi[:4]
    return kode.upper()
    

def find_court(num_ksiegi):
    kode = court_kode(num_ksiegi)
    return f'Lokalizacja sądu: {sady.kod_sad_dict[kode]}'



if __name__ == "__main__":
    app.run(debug=True)
