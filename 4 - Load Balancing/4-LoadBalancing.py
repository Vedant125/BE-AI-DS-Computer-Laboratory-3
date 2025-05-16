'''Write code to simulate requests coming from clients and 
distribute them among the servers using the load balancing 
algorithms.'''
import random

class Server:
    def __init__(self, name):
        self.name = name
        self.active_connections = 0  # Used for Least Connections

class LoadBalancer:
    def __init__(self, servers):
        self.servers = [Server(s) for s in servers]
        self.rr_index = 0  # For Round Robin

    def random_selection(self):
        return random.choice(self.servers)

    def round_robin(self):
        server = self.servers[self.rr_index % len(self.servers)]
        self.rr_index += 1
        return server

    def least_connections(self):
        return min(self.servers, key=lambda s: s.active_connections)

    def assign_request(self, strategy):
        if strategy == "random":
            server = self.random_selection()
        elif strategy == "round_robin":
            server = self.round_robin()
        elif strategy == "least_connections":
            server = self.least_connections()
        else:
            raise ValueError("Invalid strategy")

        # Simulate assigning a request
        server.active_connections += 1
        print(f"{strategy.capitalize():<15} - Request -> {server.name} (Active: {server.active_connections})")

        # Simulate request completion
        server.active_connections -= 1

def simulate_client_requests(load_balancer, num_requests):
    strategies = ["random", "round_robin", "least_connections"]
    for strategy in strategies:
        print(f"\n--- {strategy.upper()} STRATEGY ---")
        for i in range(num_requests):
            load_balancer.assign_request(strategy)

# List of server names
servers = ["Server A", "Server B", "Server C"]
load_balancer = LoadBalancer(servers)

# Simulate 5 requests per strategy
simulate_client_requests(load_balancer, 5)
