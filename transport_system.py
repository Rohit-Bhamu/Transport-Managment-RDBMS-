import mysql.connector
from mysql.connector import Error
from tabulate import tabulate
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TransportManagementSystem:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD', ''),
                database='transport_management'
            )
            print("Successfully connected to the database!")
        except Error as e:
            print(f"Error connecting to MySQL Database: {e}")

    def add_vehicle(self, vehicle_number, vehicle_type, capacity):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO vehicles (vehicle_number, vehicle_type, capacity) VALUES (%s, %s, %s)"
            cursor.execute(query, (vehicle_number, vehicle_type, capacity))
            self.connection.commit()
            print("Vehicle added successfully!")
        except Error as e:
            print(f"Error adding vehicle: {e}")
        finally:
            cursor.close()

    def add_driver(self, name, license_number, phone_number):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO drivers (name, license_number, phone_number) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, license_number, phone_number))
            self.connection.commit()
            print("Driver added successfully!")
        except Error as e:
            print(f"Error adding driver: {e}")
        finally:
            cursor.close()

    def add_route(self, route_name, start_location, end_location, distance_km, estimated_time_minutes):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO routes (route_name, start_location, end_location, distance_km, estimated_time_minutes) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (route_name, start_location, end_location, distance_km, estimated_time_minutes))
            self.connection.commit()
            print("Route added successfully!")
        except Error as e:
            print(f"Error adding route: {e}")
        finally:
            cursor.close()

    def create_booking(self, vehicle_id, driver_id, route_id, booking_date):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO bookings (vehicle_id, driver_id, route_id, booking_date) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (vehicle_id, driver_id, route_id, booking_date))
            self.connection.commit()
            print("Booking created successfully!")
        except Error as e:
            print(f"Error creating booking: {e}")
        finally:
            cursor.close()

    def view_vehicles(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM vehicles")
            vehicles = cursor.fetchall()
            headers = ["ID", "Vehicle Number", "Type", "Capacity", "Status", "Created At"]
            print(tabulate(vehicles, headers=headers, tablefmt="grid"))
        except Error as e:
            print(f"Error fetching vehicles: {e}")
        finally:
            cursor.close()

    def view_drivers(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM drivers")
            drivers = cursor.fetchall()
            headers = ["ID", "Name", "License Number", "Phone", "Status", "Created At"]
            print(tabulate(drivers, headers=headers, tablefmt="grid"))
        except Error as e:
            print(f"Error fetching drivers: {e}")
        finally:
            cursor.close()

    def view_routes(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM routes")
            routes = cursor.fetchall()
            headers = ["ID", "Route Name", "Start", "End", "Distance (km)", "Time (min)", "Created At"]
            print(tabulate(routes, headers=headers, tablefmt="grid"))
        except Error as e:
            print(f"Error fetching routes: {e}")
        finally:
            cursor.close()

    def view_bookings(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT b.booking_id, v.vehicle_number, d.name as driver_name, 
                       r.route_name, b.booking_date, b.status, b.created_at
                FROM bookings b
                JOIN vehicles v ON b.vehicle_id = v.vehicle_id
                JOIN drivers d ON b.driver_id = d.driver_id
                JOIN routes r ON b.route_id = r.route_id
            """)
            bookings = cursor.fetchall()
            headers = ["Booking ID", "Vehicle", "Driver", "Route", "Date", "Status", "Created At"]
            print(tabulate(bookings, headers=headers, tablefmt="grid"))
        except Error as e:
            print(f"Error fetching bookings: {e}")
        finally:
            cursor.close()

    def __del__(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

def main():
    tms = TransportManagementSystem()
    
    while True:
        print("\nTransport Management System")
        print("1. Add Vehicle")
        print("2. Add Driver")
        print("3. Add Route")
        print("4. Create Booking")
        print("5. View Vehicles")
        print("6. View Drivers")
        print("7. View Routes")
        print("8. View Bookings")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            vehicle_type = input("Enter vehicle type: ")
            capacity = int(input("Enter vehicle capacity: "))
            tms.add_vehicle(vehicle_number, vehicle_type, capacity)
            
        elif choice == "2":
            name = input("Enter driver name: ")
            license_number = input("Enter license number: ")
            phone_number = input("Enter phone number: ")
            tms.add_driver(name, license_number, phone_number)
            
        elif choice == "3":
            route_name = input("Enter route name: ")
            start_location = input("Enter start location: ")
            end_location = input("Enter end location: ")
            distance = float(input("Enter distance in km: "))
            time = int(input("Enter estimated time in minutes: "))
            tms.add_route(route_name, start_location, end_location, distance, time)
            
        elif choice == "4":
            vehicle_id = int(input("Enter vehicle ID: "))
            driver_id = int(input("Enter driver ID: "))
            route_id = int(input("Enter route ID: "))
            booking_date = input("Enter booking date (YYYY-MM-DD): ")
            tms.create_booking(vehicle_id, driver_id, route_id, booking_date)
            
        elif choice == "5":
            tms.view_vehicles()
            
        elif choice == "6":
            tms.view_drivers()
            
        elif choice == "7":
            tms.view_routes()
            
        elif choice == "8":
            tms.view_bookings()
            
        elif choice == "9":
            print("Thank you for using Transport Management System!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 