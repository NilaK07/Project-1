
import random 
import array 
def password_genrater(length):
    digits= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
					'z'] 

    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
					'Z'] 

    symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
		'*', '(', ')', '<']
    all = digits + lower +upper+symbol
    rand_digit = random.choice(digits) 
    rand_upper = random.choice(upper) 
    rand_lower = random.choice(lower) 
    rand_symbol = random.choice(symbol) 
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol  
    for x in range(length-4):
        temp_pass = temp_pass + random.choice(all) 
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list) 
    password = "" 
    for x in temp_pass_list:
        password = password + x 
    return password
length=int(input("enter the length:"))		
print("genrated password:",password_genrater(length)) 

