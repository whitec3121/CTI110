# This program and project finds the projected profit of the sales of a company.
#It finds 23% of total sales and marks them as profit using print and fomratiing functions.
#2/20/2020
#CTI-110-0902 P2T1 - Sales Prediction
#Carson White
#

# Get the projected total sales.
total_sales = float (input('Enter the projected sales: '))

# Calculate the profit as 23% of total sales.
profit = total_sales * 0.23

#Display the profit
print ('The profit is $', format(profit, ',.2f'))
