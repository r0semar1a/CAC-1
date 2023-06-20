class MovieBookingApp:
    def __init__(self):
        self.snacks_menu = {
            'Popcorn': 100,
            'Candy': 50,
            'Soda': 80
        }
        self.seats = [[True] * 10 for _ in range(10)]
        self.booked_seats = set()
        self.ticket_price = 30

    def display_menu(self):
        print('1. Book Ticket')
        print('2. Cancel Ticket')
        print('3. Exit')

    def display_snacks_menu(self):
        print('Snacks Menu:')
        for i, (snack, price) in enumerate(self.snacks_menu.items(), start=1):
            print(f'{i}. {snack} - ${price}')

    def display_seats(self):
        print('Available Seats:')
        for row in self.seats:
            print(' '.join('X' if seat else 'O' for seat in row))

    def book_ticket(self):
        self.display_seats()
        print('Select a seat (row, column): ')
        try:
            row = int(input())
            column = int(input())
        except ValueError:
            print('Invalid input. Please enter numeric values for row and column.')
            return

        if not self.is_seat_valid(row, column):
            print('Invalid seat selection.')
            return

        if not self.is_seat_available(row, column):
            print('Seat already booked.')
            return

        self.booked_seats.add((row, column))
        self.seats[row][column] = False

        print('Seat booked successfully.')

        self.book_snacks()

    def book_snacks(self):
        print('Do you want to book snacks? (y/n)')
        choice = input()

        if choice.lower() == 'y':
            self.display_snacks_menu()
            print('Select a snack item (enter the corresponding number): ')
            try:
                snack_choice = int(input())
            except ValueError:
                print('Invalid input. Please enter one numeric value as row and another as column.')
                return

            if snack_choice not in range(1, len(self.snacks_menu) + 1):
                print('Invalid snack selection.')
                return

            snack = list(self.snacks_menu.keys())[snack_choice - 1]
            price = self.snacks_menu[snack]

            print(f'You have selected {snack}. The price is ${price}.')
                         
            total_amount = self.ticket_price + price
            print(f'Total amount: ${total_amount}')

            print('Enter your card details:')
            while True:
                card_number = input('Card Number: ')
                cvv = input('CVV: ')

                if not card_number.isdigit() or not cvv.isdigit():
                    print('Invalid card details. Please enter only numeric values.')
                else:
                    break

            print('Payment successful.')
            print('Snacks booked successfully. \nThank you for choosing our service!')

    def cancel_ticket(self):
        self.display_seats()
        print('Select a seat to cancel (row, column): ')
        try:
            row = int(input())
            column = int(input())
        except ValueError:
            print('Invalid input. Please enter numeric values for row and column.')
            return

        if not self.is_seat_valid(row, column):
            print('Invalid seat selection.')
            return

        if (row, column) not in self.booked_seats:
            print('Seat not booked.')
            return

        self.booked_seats.remove((row, column))
        self.seats[row][column] = True

        print('Ticket canceled successfully. \nThank  you for choosing our service!')

    def is_seat_valid(self, row, column):
        return 0 <= row < len(self.seats) and 0 <= column < len(self.seats[0])

    def is_seat_available(self, row, column):
        return self.seats[row][column]

    def run(self):
        print('Welcome!')
        while True:
            self.display_menu()
            choice = input('Enter your choice: ')

            if choice == '1':
                self.book_ticket()
            elif choice == '2':
                self.cancel_ticket()
            elif choice == '3':
                break


if __name__ == '__main__':
    app = MovieBookingApp()
    app.run()