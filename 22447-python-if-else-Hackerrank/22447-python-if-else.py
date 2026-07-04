if __name__ == '__main__':
    n = int(input().strip())
    
    # Check if the number is odd
    if n % 2 != 0:
        print("Weird")
    else:
        # If the number is even, check the specific ranges
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna