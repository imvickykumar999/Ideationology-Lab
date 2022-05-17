
# https://problemsolvingwithpython.com/11-Python-and-External-Hardware/11.02-Bytes-and-Unicode-Strings/

# pip3 install --upgrade pyserial

def converted(test = 'Hello World'): 
    decrypted = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '0', ',', '?', '(', ')', '!']

    encrypted = ['/', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
                 '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
                 '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
                 '-..-', '-.--', '--..', '.----', '..---', '...--', '....-',
                 '.....', '-....', '--...', '---..', '----.', '-----', '--..--',
                 '..--..', '-.--.', '-.--.-', '-.-.--']

    morse_enc = dict(zip(decrypted, encrypted))
    morse_dec = dict([(encrypted, decrypted) for decrypted,
                      encrypted in morse_enc.items()])

    # test = request.form['morse']
    # test = input('Enter Morse Code or, Simple Text (or, just Press Ok/Enter for default entry) : ')
    if test == '':
        test = '- .... . / -.. ..- .-. .- - .. --- -. / --- ..-. / .- / -.. .- ... .... / .. ... / - .... .-. . . / - .. -- . ... / - .... . / -.. ..- .-. .- - .. --- -. / --- ..-. / .- / -.. --- - --..-- / . .- -.-. .... / -.. --- - / --- .-. / -.. .- ... .... / .-- .. - .... .. -. / .- / -.-. .... .- .-. .- -.-. - . .-. / .. ... / ..-. --- .-.. .-.. --- .-- . -.. / -... -.-- / .--. . .-. .. --- -.. / --- ..-. / ... .. --. -. .- .-.. / .- -... ... . -. -.-. . --..-- / -.-. .- .-.. .-.. . -.. / .- / ... .--. .- -.-. . --..-- / . --.- ..- .- .-.. / - --- / - .... . / -.. --- - / -.. ..- .-. .- - .. --- -. --..-- / - .... . / .-.. . - - . .-. ... / --- ..-. / .- / .-- --- .-. -.. / .- .-. . / ... . .--. .- .-. .- - . -.. / -... -.-- / .- / ... .--. .- -.-. . / --- ..-. / -.. ..- .-. .- - .. --- -. / . --.- ..- .- .-.. / - --- / - .... .-. . . / -.. --- - ... --..-- / .- -. -.. / - .... . / .-- --- .-. -.. ... / .- .-. . / ... . .--. .- .-. .- - . -.. / -... -.-- / .- / ... .--. .- -.-. . / . --.- ..- .- .-.. / - --- / ... . ...- . -. / -.. --- - ... /'

    test = test.replace("_", "-").upper()
    test_list = test.split(' ')

    decrypt = []
    def convert(j):
        for i in j:
            try:
              decrypt.append((morse_enc[i]))
            except:
              try:
                decrypt.append((morse_dec[i]))
              except:
                pass

    if not any(ele in encrypted for ele in test_list):
        box=[]
        for i in test_list:
            box.append(i+' ')
        test_list = box

        for j in test_list:
            convert(j)
            text = ' '.join(decrypt)
    else:
        convert(test_list)
        text = ''.join(decrypt)
    return text


import serial, keyboard, time                   # add Serial library for Serial communication

Arduino_Serial = serial.Serial('com8',9600)     #Create Serial port object called arduinoSerialData
print (Arduino_Serial.readline())               #read the serial data and print it as line

# -------------------------------------------

test = input('Enter a sentence to visualize in morse code : ')
con = converted(test)
print(con)

for i in con:
    Arduino_Serial.write(b'0')
    time.sleep(.2)

    if i == '.':
        print(i)
        Arduino_Serial.write(b'1')
        time.sleep(1)

    if i == '-':
        print(i)
        Arduino_Serial.write(b'1')
        time.sleep(3)

    if i == ' ':
        print(i)
        Arduino_Serial.write(b'1')
        time.sleep(1)

    if i == '/':
        print(i)
        Arduino_Serial.write(b'1')
        time.sleep(1.5)

# -------------------------------------------

# print ("Enter 1 to ON LED and 0 to OFF LED")
# while 1:                                        #infinite loop
#     input_data = input().encode()               #waits until user enters data
#     print ("you entered", input_data)           #prints the data for confirmation
#     Arduino_Serial.write(input_data)            #send 1 to arduino

# -------------------------------------------

# while True:                                       # Send 1 or 0 automatically
#     data = '1'
#     Arduino_Serial.write(data.encode())
#     print ("Data sent ", data)                    #prints the data
#     time.sleep(1)

#     data = b'0'
#     Arduino_Serial.write(data)
#     print ("Data sent ", data.decode())                    #prints the data
#     time.sleep(1)
    
#     if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#         break  # finishing the loop