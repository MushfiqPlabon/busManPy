import random

# --- Admin Credentials (Hardcoded for simplicity) ---
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

# --- Data Storage (using dictionaries and lists) ---
# Stores route information. Keys are route names (e.g., "NYC-LAX"),
# values are dictionaries containing 'origin', 'destination', 'description', and 'fare'.
# The description limit is 25 words.
all_routes = {
    "NYC-LAX": {
        'origin': 'New York City',
        'destination': 'Los Angeles',
        'fare': 150.00,
        'description': "A scenic route across the United States, connecting the East Coast to the West Coast. Enjoy diverse landscapes and vibrant cities along the way."
    },
    "LAX-SFO": {
        'origin': 'Los Angeles',
        'destination': 'San Francisco',
        'fare': 75.00,
        'description': "A popular route along the California coast, offering stunning views of the Pacific Ocean and the iconic Golden Gate Bridge."
    },
    "SFO-SEA": {
        'origin': 'San Francisco',
        'destination': 'Seattle',
        'fare': 100.00,
        'description': "A scenic route through the Pacific Northwest, featuring lush forests, rugged coastlines, and vibrant cityscapes. Experience the beauty of the West Coast."
    },
    "SEA-CHI": {
        'origin': 'Seattle',
        'destination': 'Chicago',
        'fare': 200.00,
        'description': "A cross-country route connecting the Pacific Northwest to the Midwest, passing through diverse landscapes and major cities."
    },
    "CHI-NYC": {
        'origin': 'Chicago',
        'destination': 'New York City',
        'fare': 120.00,
        'description': "A classic route connecting the heart of the Midwest to the bustling streets of New York City, offering a blend of urban and rural scenery."
    },
    "MIA-ATL": {
        'origin': 'Miami',
        'destination': 'Atlanta',
        'fare': 90.00,
        'description': "A vibrant route connecting the sunny beaches of Miami to the bustling city of Atlanta, featuring a mix of urban and coastal landscapes."
    },
    "ATL-DC": {
        'origin': 'Atlanta',
        'destination': 'Washington D.C.',
        'fare': 80.00,
        'description': "A historical route connecting the South to the nation's capital, offering a blend of Southern charm and political significance."
    },
} 

# Stores vehicle information. Keys are vehicle IDs (e.g., "V001"),
# values are dictionaries containing 'route_name', 'max_seats', and 'occupied_seats'.
all_vehicles = {
    "V001": {
        'route_name': 'NYC-LAX',
        'max_seats': 50,
        'occupied_seats': 0
    },
    "V002": {
        'route_name': 'LAX-SFO',
        'max_seats': 40,
        'occupied_seats': 0
    },
    "V003": {
        'route_name': 'SFO-SEA',
        'max_seats': 45,
        'occupied_seats': 0
    },
    "V004": {
        'route_name': 'SEA-CHI',
        'max_seats': 60,
        'occupied_seats': 0
    },
    "V005": {
        'route_name': 'CHI-NYC',
        'max_seats': 55,
        'occupied_seats': 0
    },
    "V006": {
        'route_name': 'MIA-ATL',
        'max_seats': 30,
        'occupied_seats': 0
    },
}

# Stores passenger booking records. Each item is a dictionary
# containing 'name', 'phone', 'vehicle_id_booked', and 'route_name_booked'.
all_passengers = [
    {
        'name': 'John Doe',
        'phone': '123-456-7890',
        'vehicle_id_booked': 'V001',
        'route_name_booked': 'NYC-LAX'
    },
    {
        'name': 'Jane Smith',
        'phone': '987-654-3210',
        'vehicle_id_booked': 'V002',
        'route_name_booked': 'LAX-SFO'
    },
    {
        'name': 'Alice Johnson',
        'phone': '555-123-4567',
        'vehicle_id_booked': 'V003',
        'route_name_booked': 'SFO-SEA'
    },
    {
        'name': 'Bob Brown',
        'phone': '444-987-6543',
        'vehicle_id_booked': 'V004',
        'route_name_booked': 'SEA-CHI'
    },
    {
        'name': 'Charlie White',
        'phone': '333-222-1111',
        'vehicle_id_booked': 'V005',
        'route_name_booked': 'CHI-NYC'
    },
]

# --- Helper Functions for Input Validation ---

def get_positive_float_input(prompt):
    """
    Prompts the user for a floating-point number and ensures it's positive.
    Keeps asking until valid input is received.
    """
    value = 0.0
    while True:
        try:
            input_str = input(prompt).strip()
            value = float(input_str)
            if value <= 0:
                print("Error: Value must be a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_positive_int_input(prompt):
    """
    Prompts the user for an integer and ensures it's positive.
    Keeps asking until valid input is received.
    """
    value = 0
    while True:
        try:
            input_str = input(prompt).strip()
            value = int(input_str)
            if value <= 0:
                print("Error: Value must be a positive whole number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# --- Functions for Route Management ---

def add_route():
    """
    Guides the admin to add a new travel route to our system.
    Includes input validation. AI description generation is removed.
    """
    print("\n--- Add New Route ---")
    name = input("Enter unique route name (e.g., 'NYC-LAX'): ").strip()
    
    if name in all_routes:
        print(f"Error: Route '{name}' already exists. Please choose a different name.")
        return False
    
    origin = input("Enter origin city: ").strip()
    destination = input("Enter destination city: ").strip()
    
    if not (origin and destination and name):
        print("Error: Route name, origin, and destination cannot be empty.")
        return False
    
    base_fare = get_positive_float_input("Enter base fare for this route (in units, e.g., 150.00): ")
    
    # Store route details in the 'all_routes' dictionary
    # The 'description' key is no longer stored here.
    all_routes[name] = {
        'origin': origin,
        'destination': destination,
        'fare': base_fare
    }
    print(f"Route '{name}' successfully added.")
    return True

def display_all_routes():
    """
    Shows information about all defined routes in the system.
    AI descriptions are no longer displayed as they are not generated.
    """
    if not all_routes:
        print("No routes have been defined yet.")
    else:
        print("\n--- Defined Travel Routes ---")
        for route_name, details in all_routes.items():
            # 'description_display' logic is removed
            print(f"Route Name: {route_name}, {details['origin']} to {details['destination']} (Fare: {details['fare']:.2f} units)")
        print("-----------------------------")

# --- Functions for Vehicle Management ---

def add_new_vehicle():
    """
    Guides the admin to add a new vehicle to our system and assign it to a predefined route.
    Includes input validation.
    """
    print("\n--- Add New Vehicle ---")
    vehicle_id = input("Enter unique vehicle ID (e.g., 'V001'): ").strip()
    
    if vehicle_id in all_vehicles:
        print(f"Error: Vehicle ID '{vehicle_id}' already exists. Please choose a different ID.")
        return False

    route_name = input("Enter the name of the route this vehicle will serve: ").strip()
    if route_name not in all_routes:
        print(f"Error: Route '{route_name}' not found. Please add the route first.")
        return False
    
    maximum_seating = get_positive_int_input("Enter the total number of seats for this vehicle: ")

    # Store vehicle details in the 'all_vehicles' dictionary
    all_vehicles[vehicle_id] = {
        'route_name': route_name,
        'max_seats': maximum_seating,
        'occupied_seats': 0 # Start with no seats booked
    }
    print(f"Vehicle '{vehicle_id}' assigned to route '{route_name}' with {maximum_seating} seats added successfully.")
    return True

def get_available_seats_for_vehicle(vehicle_id):
    """
    Calculates available seats for a specific vehicle.
    """
    vehicle = all_vehicles.get(vehicle_id)
    if vehicle:
        return vehicle['max_seats'] - vehicle['occupied_seats']
    return 0 # If vehicle not found, no available seats

def display_all_vehicles():
    """
    Shows information about all vehicles currently registered in the system.
    AI descriptions are no longer displayed here.
    """
    if not all_vehicles:
        print("Currently, no vehicles are registered in the system.")
    else:
        print("\n--- Current Vehicle Schedule & Availability ---")
        for vehicle_id, details in all_vehicles.items():
            route_details = all_routes.get(details['route_name'])
            route_summary = "Unknown Route"
            # 'description_display' logic is removed
            if route_details:
                route_summary = f"{route_details['origin']} to {route_details['destination']}"
            
            available = get_available_seats_for_vehicle(vehicle_id)
            print(f"Vehicle ID: {vehicle_id}, Route: {route_summary}, "
                  f"Available Seats: {available}/{details['max_seats']}")
        print("-----------------------------------------------")

# --- Functions for Ticket Booking ---

def process_ticket_booking():
    """
    Guides the user to book a ticket for a passenger on a specified vehicle.
    """
    print("\n--- Book a Ticket ---")
    requested_vehicle_id = input("Enter the Vehicle ID you wish to book on: ").strip()
    
    vehicle = all_vehicles.get(requested_vehicle_id)

    if vehicle:
        if get_available_seats_for_vehicle(requested_vehicle_id) > 0:
            passenger_name = input("Enter your full name: ").strip()
            passenger_phone = input("Enter your contact phone number: ").strip()

            # Book a seat by increasing occupied_seats
            vehicle['occupied_seats'] += 1
            
            # Record the passenger booking
            all_passengers.append({
                'name': passenger_name,
                'phone': passenger_phone,
                'vehicle_id_booked': requested_vehicle_id,
                'route_name_booked': vehicle['route_name'] # Also store route for record
            })
            
            # Retrieve fare from the vehicle's assigned route
            fare = all_routes[vehicle['route_name']]['fare']
            print(f"Ticket successfully reserved on vehicle {requested_vehicle_id}!")
            
            # Optional: Random discount feature
            if random.random() < 0.3: # 30% chance for a discount
                discount_percentage = random.randint(5, 15)
                discount_amount = fare * (discount_percentage / 100)
                final_fare = fare - discount_amount
                print(f"Original Fare: {fare:.2f} units")
                print(f"Lucky you! You got a {discount_percentage}% discount!")
                print(f"Final Booking Fare: {final_fare:.2f} units.")
            else:
                print(f"Booking Fare: {fare:.2f} units.")
        else:
            print(f"Apologies, vehicle {requested_vehicle_id} has no seats currently available.")
    else:
        print(f"Vehicle with ID '{requested_vehicle_id}' was not found in our system.")

# --- Admin Login Function ---

def admin_authenticate():
    """
    Prompts the user for admin credentials and checks if they are valid.
    Returns True if login is successful, False otherwise.
    """
    entered_username = input("Enter admin username: ").strip()
    entered_password = input("Enter admin password: ").strip()

    if entered_username == ADMIN_USERNAME and entered_password == ADMIN_PASSWORD:
        print("Administrator login successful!")
        return True
    else:
        print("Invalid credentials.")
        return False

# --- Main Program Flow ---

def main():
    """
    The main function to run the transport booking application.
    It handles user input and navigates through menus.
    """
    is_admin_logged_in = False # Flag to track admin session state

    # Main application loop that keeps running until the user chooses to exit
    while True:
        print("\n===RoutePy: Navigating Bookings===")
        print("=============Main Menu===============")
        print(f"#Admin login user is '{ADMIN_USERNAME}' and password is '{ADMIN_PASSWORD}'\n")
        print("1. Administrator Login")
        print("2. Book a Passenger Ticket")
        print("3. View Available Vehicles & Routes")
        print("4. Exit Application")
        
        user_choice = input("\nPlease enter your choice (1-4): ").strip()

        if user_choice == "1":
            if admin_authenticate():
                is_admin_logged_in = True
                # Admin specific menu loop
                while is_admin_logged_in:
                    print("\n--- Administrator Panel ---")
                    print("1. Add a New Route")
                    print("2. Add a New Vehicle")
                    print("3. View All Defined Routes")
                    print("4. View All Registered Vehicles")
                    print("5. Logout from Admin Panel")
                    
                    admin_action_choice = input("Enter your admin choice (1-5): ").strip()

                    if admin_action_choice == "1":
                        add_route()
                    elif admin_action_choice == "2":
                        add_new_vehicle()
                    elif admin_action_choice == "3":
                        display_all_routes()
                    elif admin_action_choice == "4":
                        display_all_vehicles()
                    elif admin_action_choice == "5":
                        is_admin_logged_in = False
                        print("You have successfully logged out of the administrator panel.")
                    else:
                        print("Invalid option for admin panel. Please choose a number from 1 to 5.")

        elif user_choice == "2":
            process_ticket_booking()

        elif user_choice == "3":
            # Both admin and passenger user roles can see this
            display_all_routes()
            display_all_vehicles()

        elif user_choice == "4":
            print("Thank you for using our transport booking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# This ensures that main() is called only when the script is executed directly.
if __name__ == '__main__':
    main()