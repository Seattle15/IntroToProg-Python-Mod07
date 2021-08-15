# ------------------------------------------------- #
# Title: Demo script for error handling and demonstrating appropriate usage of 'flags'
# Description: write a script that demonstrates exceptions.
#              the script will ask user to enter two integers between
#              one and 100 (inclusive) and raise exceptions when user
#              does otherwise
# ChangeLog: (Who, When, What)
#  Hedy Khalatbari, 08/14/2021, Created Script
# ------------------------------------------------- #

# -- Data -- #
strChoice = ''              # Captures the user option selection
int_1 = ''                  # Captures the user input for first number
int_2 = ''                  # Captures the user input for second number
strStatus1 = ''              # Captures the status of the first processing function
strStatus2 = ''              # Captures the status of the second processing function
list_int = []
for i in range(0, 101, 1):
    list_int.append(i)       # list of integers from 0 to 100. I included zero so that I
                             # could use the ZeroDivision exception

# -- Processing -- #
# Step 1- define function for checking the validity of the inputs
# Step 2- define function for performing the four primary arithmetics tasks

class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def inputs_to_integer(num_1, num_2):
        """
        convert to integers and ascertain that the user has correctly
        entered an integer between 1 and 100 (inclusive)
        :param num_1: first user input
        :param num_2: second user input
        :return: verified integers are returned
        """
        try:
            num_1 = int(num_1)   # turn string into integer
            num_2 = int(num_2)   # turn string into integer
            return num_1, num_2,'Task completed'
        except ValueError:
            return str(num_1), str(num_2),'Task aborted'


    @staticmethod
    def arithmetics(num_1, num_2):
        """
        function verifies that number is between 1 and 100 and then
        performs the four math tasks on numbers
        :param num_1: first integer
        :param num_2: second integer
        :return: return the results of +, -, * and /
        """
        if (num_1 in list_int) and (num_2 in list_int):
            try:
                sum = num_1 + num_2
                difference = abs(num_1 - num_2)
                product = num_1 * num_2
                division = num_1 / num_2
                return sum, difference, product, division, 'Task completed'
            except ZeroDivisionError:
                return str(num_1), str(num_1), str(num_2), str(num_2), 'Zero division'
        else:
            return str(num_1), str(num_1), str(num_2), str(num_2), 'Task aborted'


# -- Presentation (I/O) -- #
# Step 3- define functions for printing menu and capturing users input choice

class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
          Menu of Options:
          1) Perform four basic math functions
          2) Exit Program
          ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input('Which option would you like to perform? [1 or 2] - ')).strip()
        print()  # Add an extra line for looks
        return choice

# Step 4- define function for printing the results;
# will print the result of the division to two decimal point number

    @staticmethod
    def print_function(num_1, num_2, sum, difference, product, division):
        """

        :param num_1: first integer from user input
        :param num_2: second integer from user input
        :param sum: sum
        :param difference: difference
        :param product: product
        :param division: division result
        :return:
        """

        print('The sum of {} and {} is {}'.format(num_1, num_2, sum))
        print('The absolute difference of {} and {} is {}'.format(num_1, num_2, difference))
        print('The product of {} and {} is {}'.format(num_1, num_2, product))
        print('The division of {} and {} results in {:.2f}'.format(num_1, num_2, division))

# -- Main script -- #
# Step 5- use a while loop to capture user choices and call the processing and IO functions

print('\nThis script will perform addition, subtraction, multiplication, and division on two numbers.'
      '\nEnter two integers between one and 100. The second number should not be zero.')


while True:
    IO.print_menu_Tasks()
    strChoice = IO.input_menu_choice()

    if strChoice == '1':
        int_1 = input('Enter the first number: ')
        int_2 = input('Enter the second number: ')
        print()  # extra space for visuals

        int_verified_1, int_verified_2, strStatus1 = Processor.inputs_to_integer(int_1, int_2)

        if strStatus1 == 'Task completed':
            sum_1, diff_1, prod_1, div_1, strStatus2 = Processor.arithmetics(int_verified_1, int_verified_2)
            if strStatus2 == 'Task completed':
                IO.print_function(int_verified_1, int_verified_2, sum_1, diff_1, prod_1, div_1)
            elif strStatus2 == 'Zero division':
                print('Division by zero is not allowed')
            else:
                print('Numbers must be between one and 100, inclusive')
        else:
            print('Please only enter integers between 1 and 100 and refrain from entering other characters')


    elif strChoice == '2':  # Exit Program
        input('\nClick ENTER to exit!')
        break  # and Exit

    else:
        print('Please choose from menu options')









