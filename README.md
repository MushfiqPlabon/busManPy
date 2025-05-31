# Transport Booking System

This repository contains two Python implementations of a simple transport booking system: a procedural (non-OOP) version and an Object-Oriented Programming (OOP) version. The non-OOP version was created as a simplified solution for a Stanford CIP final project, while the OOP version was developed while learning OOP with Python at Phitron.

## Features

### Common Features (Both Versions)

- **Route Management**: Define and display travel routes with origin, destination, and base fare.
- **Vehicle Management**: Add and display vehicles, assign them to routes, and track their seating capacity.
- **Ticket Booking**: Allow passengers to book tickets on available vehicles.
- **Admin Panel**: Restricted access for administrators to manage routes and vehicles.
- **Input Validation**: Basic validation for numerical inputs (fares, seats) and ensuring unique IDs/names.

### Procedural (Non-OOP) Version Specifics (`busManNoOOP.py`)

- **Global Data Structures**: All data (routes, vehicles, passengers) are stored in global dictionaries and lists.
- **Direct Data Manipulation**: Functions directly modify these global data structures.
- **Random Discount Feature**: Includes a 30% chance for a random discount (5-15%) on booking fares.

### Object-Oriented (OOP) Version Specifics (`busManOOP.py`)

- **Modular Design**: Utilizes classes (`Route`, `TransportVehicle`, `Traveler`, `CentralBookingSystem`, `SystemAdministrator`) for better organization and encapsulation.
- **Encapsulation**: Data and functions that operate on that data are bundled together within classes.
- **Clearer Relationships**: Object references establish explicit relationships between entities (e.g., a `TransportVehicle` object is linked to a `Route` object).

## How to Run

1.  **Save the file**: Save either `busManNoOOP.py` or `busManOOP.py` to your local machine.
2.  **Open a terminal/command prompt**: Navigate to the directory where you saved the file.
3.  **Run the script**: Execute the script using Python:

    ```bash
    python busManNoOOP.py
    # or
    python busManOOP.py
    ```

4.  **Follow the prompts**: The application will present a menu, and you can interact with it by entering your choices.

## Admin Credentials

For both versions, the default administrator login details are:

- **Username**: `admin`
- **Password**: `1234`

## Project Structure (Conceptual)

### `busManNoOOP.py`

- `ADMIN_USERNAME`, `ADMIN_PASSWORD`: Global constants for admin login.
- `all_routes`: Global dictionary storing route data.
- `all_vehicles`: Global dictionary storing vehicle data.
- `all_passengers`: Global list storing passenger booking records.
- Helper functions for input validation (e.g., `get_positive_float_input`, `get_positive_int_input`).
- Functions for route management (e.g., `add_route`, `display_all_routes`).
- Functions for vehicle management (e.g., `add_new_vehicle`, `display_all_vehicles`, `get_available_seats_for_vehicle`).
- Function for ticket booking (`process_ticket_booking`).
- Admin authentication function (`admin_authenticate`).
- `main()`: The primary function to run the application loop and manage menus.

### `busManOOP.py`

- `TransportVehicle` Class: Manages vehicle-specific data and booking logic.
- `Route` Class: Defines route properties and provides route information.
- `Traveler` Class: Represents a passenger and their booking details.
- `CentralBookingSystem` Class: Manages all `Route`, `TransportVehicle`, and `Traveler` objects, providing methods for system-wide operations like adding, displaying, and booking.
- `SystemAdministrator` Class: Handles admin authentication.
- `main()`: Initializes class instances and orchestrates the application flow and user interface.

## Development Notes

The procedural version (`busManNoOOP.py`) offers a straightforward, top-down approach suitable for smaller projects or when a rapid, less structured implementation is preferred. The OOP version (`busManOOP.py`) showcases how to structure a program using objects, leading to more maintainable, scalable, and reusable code, which is beneficial for larger or more complex applications.

Choosing between OOP and procedural approaches often depends on the project's scale, complexity, and long-term maintainability goals. This repository provides a clear demonstration of both.
