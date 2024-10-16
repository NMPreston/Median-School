# Noah Preston, CSC-231-001

# open the file and read integers into a list
num_file = open('numbers.txt', 'r')
numbers = [] # create list
for line in num_file:
    numbers.append(int(line.strip())) # converts from strings to int & stores in list
num_file.close() # close file

# sets variables to 0 and None
count = 0
total_sum = 0
minimum = None
maximum = None

for num in numbers: # starts for loop 
    count += 1 # increments by one
    total_sum += num # adds number to the total sum 
    if minimum is None or num < minimum: # stores min number
        minimum = num
    if maximum is None or num > maximum: # stores max number
        maximum = num

# gets the average
average = total_sum / count

# print results
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Min: {minimum}")
print(f"Max: {maximum}")





