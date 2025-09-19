# def string_to_data(rle_data):
#     parts = rle_data.split(':')
#     string_to_data = []
#     for i in parts:
#         if i.isdigit(): 
#             string_to_data.append(int(i))
#         else:
#             string_to_data.append(int(i, 16))
#     return string_to_data

# def decode_rle(flat_data):
#     decode_rle = []
#     for i in range(0, len(flat_data), 2):
#         run_l = flat_data[i]
#         value = flat_data[i + 1]
#         decode_rle.extend([value] * run_l)
#     return decode_rle

# # Simulating the input
# RLE_string = "28:10:6B:10:10B:10:2B:10:12B:10:2B:10:5B:20:11B:10:6B:10"
# image_data = decode_rle(string_to_data(RLE_string))
# print(image_data)

# def count_runs(flat_data):
#     count = 1
#     additional = 1
#     for i in range(len(flat_data)-1):
#         if flat_data[i] == flat_data[i+1] and count < 15:
#             count += 1 
#         else:
#             additional += 1 
#             count = 1 
        
#     return additional
    
            
        
            
        
        

# # flat_data =  [ 9, 2, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15 ]
# flat_data = [ 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9 ]

# print(count_runs(flat_data))


# def encode_rle(flat_data):
#     encode_rle = []
#     count = 1 
#     for i in range(len(flat_data) -1):
#         if flat_data[i] == flat_data[i+1]:
#             count += 1
#             if count == 15:
#                 encode_rle.append(count) 
#                 encode_rle.append(flat_data[i]) 
#                 count = 0
#         else:
#             encode_rle.append(count)  
#             encode_rle.append(flat_data[i])  
#             count = 1 
#     encode_rle.append(count)  
#     encode_rle.append(flat_data[-1])
#     return encode_rle

    

# flat_data = [ 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9 ]




# print(encode_rle(flat_data))

# def string_to_data(rle_data):
#     # parts = rle_data.split(':')
#     string_to_data = []
    
#     # if ':' in rle_data:
#     #     parts = rle_data.split(':')
#     #     return [int(parts[0], 16), int(parts[1])]
    
#     for i in rle_data:
#         if i.isdigit(): 
#             string_to_data.append(int(i))
#         else:
#             string_to_data.append(int(i, 16))
#     return string_to_data


# rle_data = "3f:64"
# rle_data = "1912101f101f101f101f101f101f101f101f101f"
# print(string_to_data(rle_data))

#  to_rle_string([15,15,6,4]) returns the string '15f:64'
# def to_rle_string(rle_data):
#     rle_string = []
    
#     # Iterate over pairs of elements (run length and run value)
#     for i in range(0, len(rle_data), 2):
#         run_length = str(rle_data[i])
        
#         run_value = rle_data[i + 1]
#         if run_value < 10:
#             run_value_hex = str(run_value)
#         elif run_value == 10:
#             run_value_hex = "a"
#         elif run_value == 11:
#             run_value_hex = "b"
#         elif run_value == 12:
#             run_value_hex = "c"
#         elif run_value == 13:
#             run_value_hex = "d"
#         elif run_value == 14:
#             run_value_hex = "e"
#         elif run_value == 15:
#             run_value_hex = "f"
        
#         rle_string.append(run_length + run_value_hex)
    
#     return ':'.join(rle_string)
    
    
# # to_rle_string([15,15,6,4]) returns the string '15f:64'
# print(to_rle_string([15,15,6,4]))

# def string_to_rle(rle_string):
#     string_to_rle = []
#     runs = rle_string.split(":") # [15f 64]
#     for run in runs:
#         first_digit = int(run[:-1]) #15
        
#         second_digit = run[-1] #f
#         if second_digit.isdigit():
#             second_digit_run = int(second_digit)
#         elif second_digit == "a":
#             second_digit_run = 10
#         elif second_digit == "b":
#             second_digit_run = 11
#         elif second_digit == "c":
#             second_digit_run = 12
#         elif second_digit == "d":
#             second_digit_run = 13
#         elif second_digit == "e":
#             second_digit_run = 14
#         elif second_digit == "f":
#             second_digit_run = 15
#         string_to_rle.extend([first_digit, second_digit_run])
#     return string_to_rle
# print(string_to_rle("15f:64"))
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

def to_rle_string(rle_string):
    string_to_rle = []
    for i in range(0, len(rle_string), 2):
        first_digit = str(rle_string[i])
        second_digit = rle_string[i +1]
        if second_digit == "a":
            second_digit = 10
        elif second_digit == "b":
            second_digit = 11
        elif second_digit == "c":
            second_digit = 12
        elif second_digit == "d":
            second_digit = 13
        elif second_digit == "e":
            second_digit = 14
        elif second_digit == "f":
            second_digit = 15
        string_to_rle.append(first_digit + second_digit)
    return ':'.join(rle_string)
    
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

def string_to_data(rle_data):
    string_to_data = []
  
    for i in rle_data:
        if i.isdigit(): 
            string_to_data.append(int(i))
        else:
            string_to_data.append(int(i, 16))
    return string_to_data


Hex_String = input("Enter the hex string holding RLE data: ")
hex_data = decode_rle(string_to_data(Hex_String))
print(hex_data)
