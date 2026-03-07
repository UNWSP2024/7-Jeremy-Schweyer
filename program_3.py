# Program #3: US_Population
def main():
    all_entered_values = []
    # Have the user input (using a loop) various information that contains three pieces of data:
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:

    while True:
        info = input("Do you want to add information? Y/N ")
        if info == "N":
            break
        year = int(input("Enter the year: "))
        state = input("Enter the state: ")
        population = int(input("Enter the population: "))
        all_entered_values.append([year, state, population])


    if all_entered_values:
        year_to_sum = int(input("Enter a year: "))
        sum_population_for_year(all_entered_values, year_to_sum)

    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]


    # Now have the user enter a year.

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

def sum_population_for_year(all_entered_values, year_to_sum):
    total_pop = 0
    found_year = False

        # Loop through each sub-list: [year, state, population]
    for i in all_entered_values:
            # Check if the year matches the user's request
        if i[0] == year_to_sum:
            total_pop += i[2]
            found_year = True

        if found_year:
            print("The total population for the year is:", total_pop)

# Loop through and sum the populations for the appropriate year.
# e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
# or 3,421,988 if they enterd 2011 for the year to sum.

# print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()
