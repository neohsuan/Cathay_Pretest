def sort_odd_even(number_string):
    # Separate odd and even numbers
    odds = [int(n) for n in number_string if int(n) % 2 != 0]
    evens = [int(n) for n in number_string if int(n) % 2 == 0]
    
    # Sort odds in descending order and evens in ascending order
    odds.sort(reverse=True)
    evens.sort()
    
    # Combine the sorted odds and evens
    result = ''.join(map(str, odds + evens))
    
    return result

def get_valid_input():
    while True:
        user_input = input("Please enter a string of numbers (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Thank you for using the program. Goodbye!")  # 在輸入 'q' 時顯示訊息
            return None
        if user_input.isdigit():
            return user_input
        print("Invalid input. Please enter only numbers.")

def main():
    while True:
        number_string = get_valid_input()
        if number_string is None:
            break
        
        sorted_result = sort_odd_even(number_string)
        print(f"Original: {number_string}")
        print(f"Sorted:   {sorted_result}")
        print()

if __name__ == "__main__":
    main()