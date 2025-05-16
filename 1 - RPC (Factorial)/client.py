'''Design a distributed application using RPC for remote 
computation where client submits an integer value to the server 
and server calculates factorial and returns the result to the client 
program.'''

import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Take input from the user
num = int(input("Enter an integer to calculate factorial: "))

# Call the remote function
result = proxy.compute_factorial(num)

# Display result
print(f"Factorial of {num} is: {result}")


