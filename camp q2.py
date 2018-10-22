num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = [] #an array that will be used to store the user's input
result = [] #an array that will be used to store the final result
print("Type numbers between 1-9, one number at a time.\nEnter any letter to convert the numbers you entered to written form stored in an array.")
while True: #an infinite loop that will be used to collect the user's input
    try:
        input_nums = int(input()) #taking the user's input as an integer
    except:
        break #breaking the loop in case something other than an integer gets entered
    if input_nums < 10 and input_nums > 0: #checking if the integer is between 1-9
        numbers.append(input_nums) #append the input to an array
    else:
        print("Please choose a number between 1-9.")

for iter_arr in numbers:
    result.append(num_words[iter_arr - 1]) #we subtract `iter_arr` by 1 to keep the result consistent because arrays start at 0
print(result)