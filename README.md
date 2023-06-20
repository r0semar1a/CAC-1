# CAC-1

# Movie Booking App

The Movie Booking App is a command-line application that allows users to book movie tickets and snacks. It provides functionality for booking tickets, canceling tickets, and booking snacks. The app also displays the available seats in a movie theater and the snacks menu.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Functionality](#functionality)
- [Examples](#examples)

## Setup

To run the Movie Booking App, follow these steps:

1. Install Python on your system if it is not already installed. The app is written in Python 3.

2. Clone the repository or download the code files.

3. Install the required dependencies by running the following command:
   ```
   pip install pandas
   ```

## Usage

To run the Movie Booking App, execute the following command in the terminal or command prompt:

```
python movie_booking_app.py
```

## Functionality

The Movie Booking App provides the following functionality:

- Displaying the main menu with options to book a ticket, cancel a ticket, or exit the program.
- Displaying the snacks menu and allowing the user to book snacks along with the ticket.
- Displaying the available seats in the theater.
- Booking a ticket by selecting a seat.
- Canceling a previously booked ticket.
- Handling invalid inputs and displaying appropriate error messages.
- Accepting card details for payment and simulating a successful payment process.

## Examples

Example 1: Booking a ticket
```
Welcome!
1. Book Ticket
2. Cancel Ticket
3. Exit
Enter your choice: 1
Available Seats:
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
Select a seat (row, column): 
2
3
Do you want to book snacks? (y/n)
y
Snacks Menu:
1. Popcorn - $100
2. Candy - $50
3. Soda - $80
Select a snack item (enter the corresponding number): 
1
You have selected Popcorn. The price is $100.
Total amount: $130
Enter your card details:
Card Number: 1234567890123456
CVV: 123
Payment successful.
Snacks booked successfully. 
Thank you for choosing our service!
```

Example 2: Canceling a ticket
```
Welcome!
1. Book Ticket
2. Cancel Ticket
3. Exit
Enter your choice: 2
Available Seats:
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
X X X X X X X X X X
Select a seat to cancel (row, column): 
2
3
Ticket canceled successfully. 
Thank you for choosing our service!
```
