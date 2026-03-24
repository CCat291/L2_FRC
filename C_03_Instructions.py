# functions go here...
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"

def instructions():
    print(make_statement("Instructions", "🦈"))

    print('''
Instructions
    ''')

def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses'"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")

# Main routine goes here
print(make_statement("Fund Raising Calculator", "🦈"))

# Ask user if they want the instructions
print()
want_instructions = string_check("Do you want to read the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("Program continues...")