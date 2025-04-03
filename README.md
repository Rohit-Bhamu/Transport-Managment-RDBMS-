# Transport Management System

A web-based Transport Management System built with Flask and MySQL that helps manage vehicles, drivers, routes, and bookings efficiently.

## Features

### Vehicle Management
- Add, edit, and delete vehicles
- Track vehicle status (available, in_use, maintenance)
- Monitor vehicle capacity and type

### Driver Management
- Add, edit, and delete drivers
- Track driver status (available, on_duty, off_duty)
- Store driver license and contact information

### Route Management
- Add, edit, and delete routes
- Track route details including distance and estimated time
- Monitor start and end locations

### Booking Management
- Create, edit, and delete bookings
- Track booking status (pending, confirmed, completed, cancelled)
- Automatic status updates for vehicles and drivers
- Quick status change actions from the booking list

## Prerequisites

- Python 3.7 or higher
- MySQL Server
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd transport-management-system
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following variables:
```
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
```

5. Create the database and tables:
```bash
mysql -u your_mysql_username -p < database_schema.sql
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

### Creating a Booking
1. Navigate to the Bookings page
2. Fill in the booking form with:
   - Vehicle selection
   - Driver selection
   - Route selection
   - Booking date
3. Click "Create Booking"

### Managing Booking Status
You can update booking status in two ways:

1. Quick Status Updates (from booking list):
   - Pending → Confirmed: Click the check mark (✓)
   - Confirmed → Completed: Click the flag (🏁)
   - Cancel Booking: Click the X (requires confirmation)

2. Detailed Status Updates:
   - Click the edit (pencil) icon
   - Select the new status from the dropdown
   - Click "Update Booking"

### Status Colors
- Pending: Yellow
- Confirmed: Blue
- Completed: Green
- Cancelled: Red

### Automatic Status Updates
The system automatically updates vehicle and driver statuses:
- When a booking is confirmed:
  - Vehicle status changes to "in_use"
  - Driver status changes to "on_duty"
- When a booking is completed or cancelled:
  - Vehicle status changes back to "available"
  - Driver status changes back to "available"

## Project Structure

```
transport-management-system/
├── app.py                 # Main application file
├── database_schema.sql    # Database schema
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
└── templates/            # HTML templates
    ├── base.html         # Base template
    ├── index.html        # Dashboard
    ├── vehicles.html     # Vehicle management
    ├── drivers.html      # Driver management
    ├── routes.html       # Route management
    ├── bookings.html     # Booking management
    └── edit_*.html       # Edit forms
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 