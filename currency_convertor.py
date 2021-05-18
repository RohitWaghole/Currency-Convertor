def operation(currencies):

    print("\tWelcome to Currencry Convertor\t\n")
    print("Please Choose the currency among these : \n")
    [print(curr) for curr in currencies.keys()]
    currency = input("\nEnter the currency name : ")
    amount = int(input("Enter the amount in RS : "))
    price = convertor(currencies,amount,currency)
    return price,amount,currency

def convertor(currencies,amount,currency):

    return (amount*float(currencies[currency]))

def main():

    with open("currency.txt") as c:
        line = c.readlines()
    currencydictionary = {}
    for a in line:
        m = a.split("\t")
        currencydictionary[m[0]] = m[1]
    converted_price,amount,currency = operation(currencydictionary)

    print()
    print(f"\t{amount}INR is {converted_price} {currency}")

if __name__ == '__main__':
    main()
