import console_gfx

def display_menu():
    print("RLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data\n")
    
def to_hex_string(data):

    to_hex_string = []
    hex_all = {
        10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f", 
    }
    for i in data:
        if i < 10:
            to_hex_string.append(str(i))
        else:
            to_hex_string.append(hex_all[i])
    return ''.join(to_hex_string)
    
def count_runs(flat_data):
    count = 1
    additional = 1
    for i in range(len(flat_data)-1):
        if flat_data[i] == flat_data[i+1] and count < 15:
            count += 1 
        else:
            additional += 1 
            count = 1 
    return additional

def encode_rle(flat_data):
    encode_rle = []
    count = 1 
    for i in range(len(flat_data) -1):
        if flat_data[i] == flat_data[i+1]:
            count += 1
            if count >= 15:
                encode_rle.append(count) 
                encode_rle.append(flat_data[i]) 
                count = 0
        else:
            encode_rle.append(count)  
            encode_rle.append(flat_data[i])  
            count = 1 
    encode_rle.append(count)  
    encode_rle.append(flat_data[-1])
    return encode_rle

    
def get_decoded_length(rle_data):
    total = 0
    for i in range(0, len(rle_data), 2):
        if i < len(rle_data):
            total += rle_data[i]
    return total
    
   
def decode_rle(flat_data):
    if not flat_data:
        return
    decode_rle = []
    for i in range(0, len(flat_data), 2):
        run_l = flat_data[i]
        value = flat_data[i + 1]
        decode_rle.extend([value] * run_l)
    return decode_rle
        
def string_to_data(rle_data):
    string_to_data = []
    for i in rle_data:
        if i.isdigit(): 
            string_to_data.append(int(i))
        else:
            string_to_data.append(int(i, 16))
    if not string_to_data:
        return 
    return string_to_data

#  to_rle_string([15,15,6,4]) returns the string '15f:64'
def to_rle_string(rle_data):
    rle_string = []
    for i in range(0, len(rle_data), 2):
        run_length = str(rle_data[i])
        
        run_value = rle_data[i + 1]
        if run_value < 10:
            run_value_hex = str(run_value)
        elif run_value == 10:
            run_value_hex = "a"
        elif run_value == 11:
            run_value_hex = "b"
        elif run_value == 12:
            run_value_hex = "c"
        elif run_value == 13:
            run_value_hex = "d"
        elif run_value == 14:
            run_value_hex = "e"
        elif run_value == 15:
            run_value_hex = "f"
        
        rle_string.append(run_length + run_value_hex)
    
    return ':'.join(rle_string)

# Ex: string_to_rle('15f:64') returns the list of ints [15,15,6,4]

def string_to_rle(rle_string):
    string_to_rle = []
    runs = rle_string.split(":") # [15f 64]
    for run in runs:
        first_digit = int(run[:-1]) #15
        
        second_digit = run[-1] #f
        if second_digit.isdigit():
            second_digit_run = int(second_digit)
        elif second_digit == "a":
            second_digit_run = 10
        elif second_digit == "b":
            second_digit_run = 11
        elif second_digit == "c":
            second_digit_run = 12
        elif second_digit == "d":
            second_digit_run = 13
        elif second_digit == "e":
            second_digit_run = 14
        elif second_digit == "f":
            second_digit_run = 15
        string_to_rle.extend([first_digit, second_digit_run])
    return string_to_rle

def main():
    print("Welcome to the RLE image encoder!\n")
    
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    rle_string = []
    rle_data = []
    while True: 
        display_menu()  
        try:
            menu = int(input("Select a Menu Option: "))
        except EOFError:
            break
        if menu == 0: 
            break
        elif menu == 1: 
            file_name = input("Enter name of the file to load: ")
            file_data = console_gfx.load_file(file_name)
        elif menu == 2:
            file_data = console_gfx.test_image
            print("Test image data loaded.")
        elif menu == 3:
            RLE_string = input("Enter an RLE string to be decoded: ")
            rle_string = decode_rle(string_to_rle(RLE_string))
            # print(image_data)
        elif menu == 4:
            Hex_String = input("Enter the hex string holding RLE data: ")
            rle_data = decode_rle(string_to_data(Hex_String))
            # print(hex_data)
        elif menu == 5: 
            hex_string = input("Enter the hex string holding flat data: ")
            flat_data = string_to_data(hex_string)
            # print(flat_hex)
        elif menu == 6:
            print("Displaying image...")
            console_gfx.display_image(file_data)
        elif menu == 7:
            print("RLE representation: ")
            ex_rle = to_rle_string(encode_rle(rle_data))
            print(ex_rle)
        elif menu == 8:
            print("RLE hex values: ")
            rle_hex = to_hex_string(encode_rle(rle_string))  
            print(rle_hex)
        elif menu == 9:
            print("Flat hex values: ")
            hex_values = to_hex_string(rle_string)
            print(hex_values)
        else:
            print("Error! Invalid input.")
            
if __name__ == "__main__":
    main()