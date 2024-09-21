def draw_hollow_triangle():
    while True:
        user_input = input("Please enter the number of stars for the triangle base (or 'q' to quit): ").lower()
        if user_input == 'q':
            print("Thank you for using the program. Goodbye!")
            break
        
        try:
            base_stars = int(user_input)
            if base_stars <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
        except ValueError:
            print("Invalid input. Please enter a positive integer or 'q' to quit.")
            continue
        
        height = base_stars
        for i in range(height):
            for j in range(height - i - 1):
                print(" ", end="")
            for j in range(i + 1):
                if i == height - 1 or j == 0 or j == i:
                    print("*", end="")
                    if j < i:  # Add space after star except for the last one
                        print(" ", end="")
                else:
                    print("  ", end="")  # Two spaces for inner empty space
            print()
        print()

# Start the loop
draw_hollow_triangle()