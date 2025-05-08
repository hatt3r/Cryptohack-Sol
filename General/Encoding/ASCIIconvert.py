arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

result = ""
for val in arr:
    result = result + chr(val)


print("the string is ", str(result))

##This code converts an array of ASCII values into a readable string. 
# It iterates through the list arr, converts each numeric value to its corresponding character using the chr function, 
# and concatenates it to the result string.
# Finally, it prints the resulting string, which is typically in a structured format like a flag or message.