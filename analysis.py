#Goal: Create a basic educational equity analysis tool
#Method: This project asks users for school data and tells them how their school compares to a national average

def analyze_school(percent_black, funding):
    # These are made-up averages for demonstration
    average_funding_for_similar_schools = 8900  # dollars #This is prototype, the actual code will pull up actual data
    expected_score_gap = 15  # percent lower than state average

    # Compare user's school to the average
    funding_difference = average_funding_for_similar_schools - funding

    result = "Analyzing...\n\n"

    # Create feedback based on comparison
    if funding_difference > 0:
        result += f"Your school receives ${funding_difference:,} less than the average school with similar demographics.\n"
    elif funding_difference < 0:
        result += f"Your school receives ${abs(funding_difference):,} more than the average school with similar demographics.\n"
    else:
        result += "Your school receives funding equal to the average for schools with similar demographics.\n"

    result += f"Test scores in schools with your funding level are typically {expected_score_gap}% lower than the state average.\n"

    return result

def main():
    print("Welcome to Education Equity!\n")

    # Get user input and convert to integers
    try:
        percent_black = int(input("Enter the % of Black students at your school: "))
        funding = int(input("Enter per-student funding at your school ($): "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    #analyzes and show the results
    summary = analyze_school(percent_black, funding)
    print("\n" + summary)

#runs the main function
if __name__ == "__main__":
    main()

def analyze_school(percent_black, funding):
    """Compare a school's funding with national averages."""
    avg_funding = 8900  # Mock average for schools with ~65% Black students
    score_gap = 15      # Assumed % drop in test scores with low funding

    funding_diff = avg_funding - funding

    result = "\nAnalyzing...\n\n"

    if funding_diff > 0:
        result += f"Your school receives ${funding_diff:,} less than the average school with similar demographics.\n"
    elif funding_diff < 0:
        result += f"Your school receives ${abs(funding_diff):,} more than the average school with similar demographics.\n"
    else:
        result += "Your school receives funding equal to the average for similar schools.\n"

    result += f"Test scores in schools with this funding level are typically {score_gap}% lower than the state average.\n"
    return result

def get_school_input():
    """Get and validate input from user."""
    try:
        percent_black = int(input("Enter the % of Black students at your school: "))
        funding = int(input("Enter per-student funding at your school ($): "))
        return percent_black, funding
    except ValueError:
        print("Invalid input. Please enter whole numbers.\n")
        return None, None

def main():
    print("Welcome to Education Equity!")
    print("This tool compares your school's funding to national averages.\n")

    report_count = 0

    print(f"\nYou analyzed {report_count} school(s). Thank you for using Education Equity!")

if __name__ == "__main__":
    main()
