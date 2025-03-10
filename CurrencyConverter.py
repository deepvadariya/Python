from forex_python.converter import CurrencyRates

def currency_converter():
    c = CurrencyRates()
    
    print("Welcome to the Currency Converter!")
    
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the source currency (e.g., USD): ").upper()
        to_currency = input("Enter the target currency (e.g., EUR): ").upper()
        
        converted_amount = c.convert(from_currency, to_currency, amount)
        
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    currency_converter()
