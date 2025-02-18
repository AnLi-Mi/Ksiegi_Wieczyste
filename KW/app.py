from flask import Flask, render_template, request
import sady


app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    control_digit = ''
    court_location = ''
    court_code = ''
    numbers = ''
    error=''
    edited_full_books_code = ''
    
    if request.method=="POST" and 'numer_ksiegiw' in request.form:
        court_code = request.form.get('court')
        court_code = court_code.upper()
        numbers = request.form.get('numer_ksiegiw')
     
        full_books_code = court_code+numbers
            
        edited_full_books_code=full_books_code.replace(" ", "")
        edited_full_books_code=edited_full_books_code.replace("/", "")

        try:
            if (int(numbers) or numbers in ['0', '00','000','0000','00000','000000','0000000','00000000']) and court_code in sady.list_kod and len(edited_full_books_code)<= 12 :
                control_digit = decoding(edited_full_books_code, encoding_key_for_kw)
                court_location = find_court(court_code)
            elif court_code not in sady.list_kod:
                error= "Błąd - Błędny identyfikator sądu prowadzącego księgę"
            elif len(edited_full_books_code)> 12:
                error= "Błąd - Wpisany identyfikator księgi jest za długi"
        except ValueError: 
                error = "Błąd - Identyfikator księgi składa się tylko z cyfr"

        
    return render_template("index.html", court_code = court_code, edited_full_books_code=edited_full_books_code, error = error, control_digit = control_digit, court_location = court_location, numbers=numbers)

# creating the dictionary with letters and digits as keys and thier encoding result as values
def encoding_key_for_kw():

    #preparing lists of elemets before and after encoding
    #in order to turn them into a dictionary by zipping later
    entered_element=[]
    returned_element=[]

    # each letter's result after encoding is it's position in aphabet +10
    # (staring from 1, not 0)
    for letter in 'xabcdefghijklmnoprstuwyz':
        entered_element.append(letter)
        returned_element.append('xabcdefghijklmnoprstuwyz'.index(letter)+10)

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
    return f"Cyfra kontrolna księgi wieczystej {(numer_ksiegi[:4] + '/' + numer_ksiegi[4:]).upper()!r}: {sum(total)%10}"

def find_court(kode):
    return f'Lokalizacja sądu: {sady.kod_sad_dict[kode]}'



if __name__ == "__main__":
    app.run(debug=True)
