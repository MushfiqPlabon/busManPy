class TransportVehicle:
    """
    Represents a single transport vehicle, typically a bus in this system.
    It manages its unique identification, the route it operates on,
    its seating capacity, and how many seats are currently booked.
    Each vehicle is assigned a specific route with a predefined fare.
    """
    def __init__(self, vehicle_id, route_obj, maximum_seating):
        """
        Initializes a new transport vehicle instance.

        Args:
            vehicle_id (str): A unique identifier for the vehicle (e.g., "BUS001").
            route_obj (Route): The Route object detailing the vehicle's origin, destination, and fare.
            maximum_seating (int): The total number of seats available on the vehicle.
        """
        self.vehicle_id = vehicle_id
        # The route_obj links this vehicle to a predefined route with its fare
        self.assigned_route = route_obj
        self.maximum_seating = maximum_seating
        self.occupied_seats = 0 # Keeps track of currently taken seats

    def get_available_seats(self):
        """
        Calculates and returns the number of seats that are still open for booking.
        """
        return self.maximum_seating - self.occupied_seats

    def reserve_seat(self):
        """
        Attempts to book one seat on the vehicle.
        If there are available seats, it reserves one and returns True.
        Otherwise, it returns False, indicating no seats could be booked.
        """
        if self.get_available_seats() > 0:
            self.occupied_seats += 1
            return True  # Seat successfully reserved
        else:
            return False # No seats left to reserve

class Route:
    """
    Represents a defined travel route with an origin, destination, and associated fare.
    Routes are independent entities that buses can be assigned to.
    """
    def __init__(self, name, origin, destination, base_fare):
        """
        Initializes a new route.

        Args:
            name (str): A unique name for the route (e.g., "CityA-CityB").
            origin (str): The starting point of the route.
            destination (str): The ending point of the route.
            base_fare (float): The base fare for this route in abstract currency units.
        """
        self.name = name
        self.origin = origin
        self.destination = destination
        self.base_fare = base_fare

    def get_route_info(self):
        """
        Returns a string summarizing the route details.
        """
        return f"{self.origin} to {self.destination} (Fare: {self.base_fare:.2f} units)"

class Traveler:
    """
    Represents a passenger who wishes to book a seat on a transport vehicle.
    Stores personal details and a reference to the specific vehicle and route they booked.
    """
    def __init__(self, full_name, contact_number, booked_vehicle_instance):
        """
        Initializes a new passenger.

        Args:
            full_name (str): The name of the traveler.
            contact_number (str): The traveler's phone number.
            booked_vehicle_instance (TransportVehicle): The specific vehicle object
                                                        the passenger booked a seat on.
        """
        self.full_name = full_name
        self.contact_number = contact_number
        self.booked_vehicle = booked_vehicle_instance # Link to the vehicle instance they booked

class CentralBookingSystem:
    """
    Manages all registered transport vehicles, defined routes, and passenger bookings.
    Handles operations like defining routes, adding vehicles, processing tickets,
    and displaying information.
    """
    def __init__(self):
        """
        Initializes the central booking system with empty dictionaries/lists
        for routes, vehicles, and passenger records.
        """
        self.routes = {} # Stores Route objects, keyed by route name
        self.fleet_of_vehicles = {} # Stores TransportVehicle objects, keyed by vehicle_id
        self.customer_records = [] # A list to store all Traveler objects

    def add_route(self, name, origin, destination, base_fare):
        """
        Adds a new route to the system.

        Args:
            name (str): Unique name for the route.
            origin (str): Starting point of the route.
            destination (str): Ending point of the route.
            base_fare (float): The base fare for this route.
        Returns:
            bool: True if route was added, False if name already exists.
        """
        if name in self.routes:
            print(f"Error: Route '{name}' already exists. Please choose a different name.")
            return False
        if not (origin and destination and name and base_fare > 0):
            print("Error: Route name, origin, destination, and a positive fare are required.")
            return False
        
        new_route = Route(name, origin, destination, base_fare)
        self.routes[name] = new_route
        print(f"Route '{name}' ({new_route.get_route_info()}) successfully added.")
        return True

    def add_new_vehicle(self, vehicle_id, route_name, maximum_seating):
        """
        Creates a new vehicle and adds it to the system's fleet,
        assigning it to a predefined route.

        Args:
            vehicle_id (str): Unique ID for the new vehicle.
            route_name (str): The name of the predefined route this vehicle will serve.
            maximum_seating (int): Total seats for the new vehicle.
        Returns:
            bool: True if vehicle added, False otherwise (e.g., route not found).
        """
        if vehicle_id in self.fleet_of_vehicles:
            print(f"Error: Vehicle ID '{vehicle_id}' already exists. Please choose a different ID.")
            return False

        if route_name not in self.routes:
            print(f"Error: Route '{route_name}' not found. Please add the route first.")
            return False
        
        if maximum_seating <= 0:
            print("Error: Maximum seating must be a positive number.")
            return False

        assigned_route_obj = self.routes[route_name]
        # Create a new TransportVehicle object, linking it to the Route object
        new_vehicle = TransportVehicle(vehicle_id, assigned_route_obj, maximum_seating)
        self.fleet_of_vehicles[vehicle_id] = new_vehicle
        print(f"Vehicle '{vehicle_id}' assigned to route '{route_name}' with {maximum_seating} seats added successfully.")
        return True

    def process_ticket_booking(self, desired_vehicle_id, customer_name, customer_phone):
        """
        Attempts to book a ticket for a customer on a specified vehicle.
        Finds the vehicle by its ID, checks availability, and if successful,
        creates a passenger record and displays the fare.
        """
        vehicle_to_book = self.fleet_of_vehicles.get(desired_vehicle_id)

        if vehicle_to_book:
            if vehicle_to_book.reserve_seat():
                # Booking is successful, create a new Traveler object
                new_passenger = Traveler(customer_name, customer_phone, vehicle_to_book)
                self.customer_records.append(new_passenger)
                # Retrieve fare from the vehicle's assigned route
                fare = vehicle_to_book.assigned_route.base_fare
                print(f"Ticket successfully reserved on vehicle {desired_vehicle_id}!")
                print(f"Booking Fare: {fare:.2f} units.")
                return
            else:
                print(f"Apologies, vehicle {desired_vehicle_id} has no seats currently available.")
                return
        else:
            print(f"Vehicle with ID '{desired_vehicle_id}' was not found in our system.")

    def display_all_routes(self):
        """
        Shows information about all defined routes in the system.
        """
        if not self.routes:
            print("No routes have been defined yet.")
        else:
            print("\n--- Defined Travel Routes ---")
            for route_name, route_obj in self.routes.items():
                print(f"Route Name: {route_name}, {route_obj.get_route_info()}")
            print("-----------------------------")

    def display_all_vehicles(self):
        """
        Shows information about all vehicles currently registered in the system,
        including their ID, assigned route, and how many seats are still open.
        """
        if not self.fleet_of_vehicles:
            print("Currently, no vehicles are registered in the system.")
        else:
            print("\n--- Current Vehicle Schedule & Availability ---")
            for vehicle_id, vehicle_obj in self.fleet_of_vehicles.items():
                route_summary = vehicle_obj.assigned_route.get_route_info()
                print(f"Vehicle ID: {vehicle_id}, Route: {route_summary}, "
                      f"Available Seats: {vehicle_obj.get_available_seats()}/{vehicle_obj.maximum_seating}")
            print("-----------------------------------------------")


class SystemAdministrator:
    """
    Handles administrative access for managing the booking system.
    Requires a specific username and password for login.
    """
    def __init__(self):
        """
        Sets the default administrative login credentials.
        """
        self.admin_username = "admin"
        self.admin_password = "1234"

    def authenticate(self):
        """
        Prompts the user for admin credentials and checks if they are valid.
        Returns True if login is successful, False otherwise.
        """
        entered_username = input("Enter admin username: ").strip()
        entered_password = input("Enter admin password: ").strip()

        if entered_username == self.admin_username and entered_password == self.admin_password:
            print("Administrator login successful!")
            return True
        else:
            print("Invalid credentials.")
            return False

# --- Program Execution Flow ---

def main():
    """
    The main function to run the transport booking application.
    It sets up the system, handles user input, and navigates through menus.
    """
    # Initialize our central booking system and the administrator account
    system_manager = CentralBookingSystem()
    admin_user = SystemAdministrator()
    is_admin_logged_in = False # Flag to track admin session state

    # Main application loop that keeps running until the user chooses to exit
    while True:
        print("\n===RoutePy: Navigating Bookings===")
        print("=============Main Menu===============")
        print("#Admin login user is admin and password is 1234\n")
        print("1. Administrator Login")
        print("2. Book a Passenger Ticket")
        print("3. View Available Vehicles & Routes") # Combined for user convenience
        print("4. Exit Application")
        
        user_choice = input("\nPlease enter your choice (1-4): ").strip()

        if user_choice == "1":
            # Attempt to log in as administrator
            if admin_user.authenticate():
                is_admin_logged_in = True # Set flag to True if login succeeds
                # Enter the admin specific menu loop
                while is_admin_logged_in:
                    print("\n--- Administrator Panel ---")
                    print("1. Add a New Route")
                    print("2. Add a New Vehicle")
                    print("3. View All Defined Routes")
                    print("4. View All Registered Vehicles")
                    print("5. Logout from Admin Panel")
                    
                    admin_action_choice = input("Enter your admin choice (1-5): ").strip()

                    if admin_action_choice == "1":
                        # Add a new route
                        route_name = input("Enter unique route name (e.g., 'NYC-LAX'): ").strip()
                        origin_city = input("Enter origin city: ").strip()
                        destination_city = input("Enter destination city: ").strip()
                        try:
                            fare_input = input("Enter base fare for this route (in units, e.g., 150.00): ").strip()
                            base_fare = float(fare_input)
                            if base_fare <= 0:
                                print("Fare must be a positive number.")
                            else:
                                system_manager.add_route(route_name, origin_city, destination_city, base_fare)
                        except ValueError:
                            print("Invalid input for fare. Please enter a numerical value.")

                    elif admin_action_choice == "2":
                        # Add a new vehicle and assign it to an existing route
                        vehicle_id = input("Enter unique vehicle ID (e.g., 'V001'): ").strip()
                        route_name = input("Enter the name of the route this vehicle will serve: ").strip()
                        try:
                            total_vehicle_seats = int(input("Enter the total number of seats for this vehicle: ").strip())
                            system_manager.add_new_vehicle(vehicle_id, route_name, total_vehicle_seats)
                        except ValueError:
                            print("Invalid input for seats. Please enter a whole number.")

                    elif admin_action_choice == "3":
                        # Display all defined routes
                        system_manager.display_all_routes()

                    elif admin_action_choice == "4":
                        # Display all registered vehicles
                        system_manager.display_all_vehicles()

                    elif admin_action_choice == "5":
                        # Logout from the admin panel
                        is_admin_logged_in = False
                        print("You have successfully logged out of the administrator panel.")
                    else:
                        print("Invalid option for admin panel. Please choose a number from 1 to 5.")

        elif user_choice == "2":
            # Option for passengers to book a ticket
            requested_vehicle_id = input("Enter the Vehicle ID you wish to book on: ").strip()
            passenger_name = input("Enter your full name: ").strip()
            passenger_phone = input("Enter your contact phone number: ").strip()
            system_manager.process_ticket_booking(requested_vehicle_id, passenger_name, passenger_phone)

        elif user_choice == "3":
            # View all available vehicles and their routes
            system_manager.display_all_routes() # Show routes first for context
            system_manager.display_all_vehicles()

        elif user_choice == "4":
            # Exit the application
            print("Thank you for using our transport booking system. Goodbye!")
            break # Breaks out of the main while loop, ending the program

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# This ensures that main() is called only when the script is executed directly.
if __name__ == '__main__':
    main()