# Structuring Python Code for Readability and Reuse

# -----------------------
# SECTION 1: Helper Functions
# -----------------------

def calculate_sum(numbers_list):
    """Return the sum of a list of numbers."""
    return sum(numbers_list)


def calculate_average(numbers_list):
    """Return the average of a list of numbers."""
    total = calculate_sum(numbers_list)
    count = len(numbers_list)
    return total / count


def display_results(total, average):
    """Display calculated results."""
    print("Total:", total)
    print("Average:", average)


# -----------------------
# SECTION 2: Main Execution
# -----------------------

def main():
    # Input data (can be replaced later with file/database input)
    sample_data = [10, 20, 30, 40]

    # Processing
    total_value = calculate_sum(sample_data)
    average_value = calculate_average(sample_data)

    # Output
    display_results(total_value, average_value)


# -----------------------
# SECTION 3: Entry Point
# -----------------------

if __name__ == "__main__":
    main()