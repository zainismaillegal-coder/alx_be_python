from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(num_days)
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")

if __name__ == "__main__":
    main()
