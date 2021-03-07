# a simple and small app that converts numbers to morse code
base_tuple = (("1", ".----"),("2", "..---"),("3", "...--"),("4", "....-"),("5", "....."),("6", "-...."),("7", "--..."),("8", "---.."),("9", "----."),("0", "-----"))
results_list = []

def convert_to_morse(entry):
    given_code = list(entry)

    for j in given_code:
        for thingns in base_tuple:
            if j == thingns[0]:
                j = thingns[1]
                #convert = results_list.replace(j, thingns[1])
                print(j) 