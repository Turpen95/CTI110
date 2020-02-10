    #SalesPrediction
    #February 3, 2020
    #CTI-110 P2T1 - Sales Prediction
    #Matthew Turpen
    #

def main():

    #INPUT
    #Get the projected total sales.
    total_sales = float(input('Enter the projected sales: '))


    #PROCESS
    #Calculate the profit as 23 percent of total sales.
    profit = total_sales * 0.23

    #OUTPUT
    #Display the profit
    print('The profit is $', format(profit, ',.2f'))
    
main()
