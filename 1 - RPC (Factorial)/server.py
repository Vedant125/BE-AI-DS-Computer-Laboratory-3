'''Design a distributed application using RPC for remote 
computation where client submits an integer value to the server 
and server calculates factorial and returns the result to the client 
program.'''

from xmlrpc.server import SimpleXMLRPCServer

# Define a function to compute factorial
def factorial(n):
    if n < 0:
        return "Error: Negative number not allowed"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")

# Register the factorial function
server.register_function(factorial, "compute_factorial")

# Run the server
server.serve_forever()
