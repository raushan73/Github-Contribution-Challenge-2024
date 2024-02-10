# Determines if a given year is a leap year (with errors)

def is_leap_year(year):
    """Checks if a given year is a leap year.

    Args:
        year: The year to check.

    Returns:
        True if the year is a leap year, False otherwise.
    """

    if year % 400 == 0:  # Incorrect leap year condition (missing divisibility by 4)
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Example usage
year = 2100
leap_year_status = is_leap_year(year)
print(f"{year} is a leap year: {leap_year_status}")
