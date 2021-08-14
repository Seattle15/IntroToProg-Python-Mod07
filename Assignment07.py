# ------------------------------------------------- #
# Title: Demo script for pickling and error handling
# Description: write a script that demonstrate pickling
# ChangeLog: (Who, When, What)
#  Hedy Khalatbari, 08/13/2021, Created Script
# ------------------------------------------------- #

# -- Data -- #
import pickle

list_steps_daily = [1000, 1500, 2000, 2500, 3000, 3000, 2500, 2000, 1500, 1000]
list_dates = ['080121', '080221', '080321', '080421', '080521', '080621', '080721',
              '080821', '080921', '081021']
file_name = 'pickled.txt'                 # text file to save the pickled data in
pickled_input = open(file_name, 'wb')     # creates/opens file in write mode (erases content)
pickled_input.close()

# -- Processing -- #
# function for pickling an object and saving it to the file
def pickle_to_file(obj_to_pickle):
    with open(file_name, 'ab') as pickled_input:
        pickle.dump(obj_to_pickle,pickled_input, pickle.HIGHEST_PROTOCOL)
    message = 'Object was pickled'
    return message

# function for unpickling all saved objects from the file into a list
def unpickle_from_file(file):
    objects = []      # defines the list to save the objects in
    with (open(file, "rb")) as pickled_output:
        while True:
            try:
                objects.append(pickle.load(pickled_output))
            except EOFError:    #  exception handling error raised in scenarios such as
                                # interruption of the input () function
                break
    return objects

# -- Presentation (I/O) -- #
# the presentation demonstrates the steps in running the script and informs the user to check the pickled.txt
# file for the pickled version of the data
print('The number of daily steps documented in the Health App in my iPhone in the first ten days of August are:')
print(list_dates)
print(list_steps_daily)
print('\nProgram will pickle these lists.')
input('Click ENTER to continue...')
pickle_to_file(list_dates)
message = pickle_to_file(list_steps_daily)
print(message)

print('Program will now unpickle these lists.')
input('Click ENTER to continue...\n')
object_list = unpickle_from_file(file_name)
print('The unpickled lists are:')
for list in object_list:
    print(list)


print('\nYou can check the pickled version in the pickled.txt file')
input('Click ENTER to exit!')

