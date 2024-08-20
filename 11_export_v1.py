import pandas
import random
import datetime import date

# lists to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_tickets_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_tickets_costs,
    "Surcharge": surcharge
}
# create frame
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total tickets cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# choose winner and look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# **** Get current date for heading and file name ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime{"%m"}
year = today.strftime{"%Y"}

heading = "---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ---- \n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# Change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create strings for printing
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
all_ticket_sales = "Total Ticket Sales: ${}".format(total)
total_profit = "Total Profit : ${}".format(profit)

# edit text below, It needs work if we have unsold tickets
sales_status = "\n*** All the tickets have been sold ***"

winner_heading ="\n---- Raffle Winner -----"
winner_text = "The winner of the raffle is {}. " \
                "They have won ${}. ie: Their ticket is " \
                "free!".format(winner_name, total_won)

# list holding content / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

