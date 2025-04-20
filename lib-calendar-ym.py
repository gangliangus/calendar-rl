import calendar

def print_calendar(year, month):
  """Prints the calendar for the given year and month."""
  try:
    year = int(year)
    month = int(month)
    if month < 1 or month > 12:
      raise ValueError("Month must be between 1 and 12")
    print(calendar.month(year, month))
  except ValueError as e:
    print(f"Invalid input: {e}")

if __name__ == "__main__":
  year = input("Enter year: ")
  month = input("Enter month: ")
  print_calendar(year, month)
