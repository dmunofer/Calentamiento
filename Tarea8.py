#Tarea 8

"""
In this project, you'll create a program that that tells
you when the value of your Bitcoin falls below $30,000.
You will need to:
- Create a function to convert Bitcoin to €
- If your Bitcoin falls below 30,000€ print a message.
You can assume that 1 Bitcoin is worth 40,000€
===> You've redeemed a hint. Replace the _'s with code to complete
this exercise.
"""
investment_in_bitcoin = 1.2
bitcoin_to_euros = 25000
# 1) write a function to calculate bitcoin to euros
def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value
investment_in_euros = bitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros )
if investment_in_euros <= 30000:
    print("Investment below 30,000€! SELL!")
else:
    print("Investment above 30,000€")











