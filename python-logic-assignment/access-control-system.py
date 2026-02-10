# Take age input
age = int(input("Enter your age: "))

# Take ID input and handle incorrect boolean values
has_id_input = input("Do you have an ID card? (True/False): ").strip().lower()

if has_id_input == "true":
    has_id = True
elif has_id_input == "false":
    has_id = False
else:
    print("Invalid input for ID. Please enter True or False.")
    exit()

# Access control check
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
20