"Final solution"
import math
def exchange_money(budget, exchange_rate):
    return budget / exchange_rate
def get_change(budget, exchanging_value):
    return budget - exchanging_value
def get_value_of_bills(denomination, number_of_bills):
    return number_of_bills * denomination
def get_number_of_bills(budget, denomination):
    return budget // denomination
def get_leftover_of_bills(budget, denomination):
    return budget % denomination
def exchangeable_value(budget, exchange_rate, spread, denomination):
    rate_with_spread = (exchange_rate * spread/100) + exchange_rate
    rate = budget/rate_with_spread
    return (math.floor(rate/denomination)) * denomination
