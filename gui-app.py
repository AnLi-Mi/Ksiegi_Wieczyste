from tkinter import *

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
def decoding(num_ksiegi, decoder):
    # editing users input so it's we can perform further operations on it
    numer_ksiegi=num_ksiegi.replace(" ", "")
    numer_ksiegi=numer_ksiegi.replace("/", "")
    numer_ksiegi=numer_ksiegi.lower()

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
    return f'Cyfra kontrolna księgi {num_ksiegi!r} to {sum(total)%10}'

#------- Creating the GUI ----------------

window = Tk()
window.title("Księgi Wieczyste")

empty_row1 = Label (window)
empty_row1.pack()

input_command = Label (window, text = "Wpisz bazę numeru Księgi Wieczystej: ")
input_command.pack()

empty_row2 = Label (window)
empty_row2.pack()

user_input = Entry (window)
user_input.pack()

empty_row3 = Label (window)
empty_row3.pack()

def submit_button_action():
    ksiega_wieczysta=user_input.get()
    response = Label(window, text = decoding(ksiega_wieczysta, encoding_key_for_kw))
    response.pack()

submit_button = Button (window, text = "Sprawdź cyfrę kontrolną", command = submit_button_action)
submit_button.pack()

empty_row4 = Label (window)
empty_row4.pack()

window.mainloop()
