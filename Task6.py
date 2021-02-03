import math
def sales_prediction():
    sum_sales = (float(input()))
    income =  sum_sales+ sum_sales*23/100
    print(income)




def pound_to_kilogram():
    pound_const = 0.454
    mass_pound = float(input())
    mass_kg = mass_pound * pound_const
    mass_tonne = mass_kg / 1000
    mass_gram = mass_kg*1000
    print(mass_gram)
    print(mass_kg)
    print(mass_tonne)
    




def cashier():
    product_1 = float(input())
    product_2 = float(input())
    product_3 = float(input())
    product_4 = float(input())
    product_5 = float(input())
    busket_sum = product_1+product_2+product_3+product_4+product_5
    busket_tax = busket_sum *7/100
    total = busket_sum+busket_tax
    print(int(busket_sum))
    print(busket_tax)
    print(total)


def odometer():
    Speed = float(input())
    Time = float(input())
    Distance = Speed*Time
    print(int(Distance))



def payment_instalments():
    sum_purchase = float(input())
    amount_payment = int(input())
    total_sum_purchase = sum_purchase * 1.05
    sum_payment = total_sum_purchase / amount_payment
    print(total_sum_purchase)
    print(sum_payment)


def miles_per_galon():
    Miles_driven = float(input())
    Gallons_used = float(input())
    MPG = Miles_driven / Gallons_used
    print('{:.1f}'.format(MPG))


def cookie():
    num_of_cookies = int(input())
    sugar = (1.5/48) *num_of_cookies
    butter = (1/48) * num_of_cookies
    flour = (2.75/48) * num_of_cookies
    print(sugar)
    print(butter)
    print(flour)




def vineyard():
    raw_length = float(input())
    raw_length_pillar = float(input())
    distance_btw_bush = float(input())
    amount_of_bushes = (raw_length-2*raw_length_pillar)/(distance_btw_bush)
    print(int(amount_of_bushes))

    

def compound_interest():
    general_amount = float(input())
    year_interest_rate = float(input())
    year_interest_rate =  year_interest_rate / 100
    amount_of_times = int(input())
    time = int(input())
    final_sum = general_amount*((1+year_interest_rate/amount_of_times)**(amount_of_times*time))
    print(final_sum)



if __name__ == "__main__":
    #eval(input() + "()")
    func = input()
    if func == "sales_prediction":
        sales_prediction()
    elif func == "pound_to_kilogram":
        pound_to_kilogram()
    elif func == "cashier":
        cashier()
    elif func == "odometer":
        odometer()
    elif func =="payment_instalments":
        payment_instalments()
    elif func == "miles_per_galon":
        miles_per_galon()
    elif func == "cookie":
        cookie()
    elif func == "vineyard":
        vineyard()
    elif func == "compound_interest":
        compound_interest()