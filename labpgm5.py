# Program to calculate Simple Interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Display the result
print("Simple Interest =", simple_interest)