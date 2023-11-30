# define sum_of_squares
sum_of_squares = 0
# define sum = 0
sum = 0
# define i = 1
# i = 1 # not required in for loop

# while 1 <= 100
# while i <= 100:
# for loop example
for i in range(1, 101): # i is defined in for loop so no need to express a variable value
    # sum_of_squares = sum_of_squares + i * i 
    sum_of_squares += i * i
    # sum = sum + i
    sum += i
    # i = i + 1
    # i += 1 # not required in for loop

# suare_of_sum = sum * sum
square_of_sum = sum * sum
# diff = square_of_sum - sum_of_square
diff = square_of_sum - sum_of_squares
# display diff
print(diff)