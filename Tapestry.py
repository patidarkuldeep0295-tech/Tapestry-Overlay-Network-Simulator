# Tapestry Overlay Network Simulator
# Distributed Computing Tiny Project

from collections import deque


class TapestrySimulator:

    def __init__(self):
        self.network = {
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "D"],
            "D": ["B", "C", "F"],
            "E": ["B", "F"],
            "F": ["D", "E"]
        }

    def display_nodes(self):
        print("\n--- Available Network Nodes ---")
        for node in self.network:
            print(f"Node {node}")

    def display_network(self):
        print("\n--- Network Connections ---")
        for node, connections in self.network.items():
            print(f"Node {node} --> {', '.join(connections)}")

    def display_routing_table(self):
        print("\n--- Routing Table ---")
        for node, connections in self.network.items():
            print(f"Node {node}: {connections}")

    def find_route(self, source, destination):
        if source not in self.network or destination not in self.network:
            return None

        queue = deque([[source]])
        visited = {source}

        while queue:
            path = queue.popleft()
            current_node = path[-1]

            if current_node == destination:
                return path

            for neighbor in self.network[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])

        return None

    def send_message(self):
        source = input("Enter source node: ").strip().upper()
        destination = input("Enter destination node: ").strip().upper()

        if source not in self.network or destination not in self.network:
            print("Error: Invalid node! Please select A, B, C, D, E or F.")
            return

        message = input("Enter your message: ")

        print("\nSearching for the route...")
        route = self.find_route(source, destination)

        if route:
            print("\n--- Message Routing Result ---")
            print("Source:", source)
            print("Destination:", destination)
            print("Message:", message)
            print("Route:", " -> ".join(route))
            print("Total Hops:", len(route) - 1)
            print("Status: Message Delivered Successfully!")

            print("\n--- Routing Steps ---")
            for i, node in enumerate(route):
                if i < len(route) - 1:
                    print(f"Node {node} forwards the message to Node {route[i + 1]}")
                else:
                    print(f"Node {node} received the message.")

        else:
            print("Message delivery failed!")

    def run(self):
        while True:
            print("\n========================================")
            print("   TAPESTRY OVERLAY NETWORK SIMULATOR")
            print("========================================")
            print("1. Display Network Nodes")
            print("2. Display Network Connections")
            print("3. Display Routing Table")
            print("4. Send Message")
            print("5. Exit")
            print("========================================")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                self.display_nodes()

            elif choice == "2":
                self.display_network()

            elif choice == "3":
                self.display_routing_table()

            elif choice == "4":
                self.send_message()

            elif choice == "5":
                print("Thank you for using Tapestry Simulator!")
                break

            else:
                print("Invalid choice! Please enter a number from 1 to 5.")


if __name__ == "__main__":
    simulator = TapestrySimulator()
    simulator.run()