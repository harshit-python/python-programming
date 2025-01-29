# Complete the print_full_name function.

def print_full_name(first, last):
    output_string = f"Hello {first} {last}! You just delved into python."
    print(output_string)

first = input("Enter first name: ").strip()
last = input("Enter last name: ").strip()
print_full_name(first, last)