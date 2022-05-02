# Name - Niranjan Sundararajan
# Roll No - 2020090

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


# Write the code here for creating an interactive program.

from a2 import *

def greetings():

    print("""Hello user! Welcome to this program. I will guide you through using it. It's simple, you'll catch on.

There are many queries that you can ask in this program, they have to be called by you. Here is a list of the various functions you can perform.

---------------------------------------------------------------------------------------------------
 CODE |         FUNCTION NAME         |                    PARAMETERS (ORDERED)
---------------------------------------------------------------------------------------------------
   1  | read_data_from_file           | (file_path="data.json") (You don't need to enter anything)
   2  | filter_by_first_name          | (records, first_name)
   3  | filter_by_last_name           | (records, last_name)
   4  | filter_by_full_name           | (records, full_name)
   5  | filter_by_age_range           | (records, min_age, max_age)
   6  | count_by_gender               | (records)
   7  | filter_by_address             | (records, address)
   8  | find_alumni                   | (records, institute_name)
   9  | find_topper_of_each_institute | (records)
  10  | find_blood_donors             | (records, receiver_person_id)
  11  | get_common_friends            | (records, list_of_ids)
  12  | is_related                    | (records, person_id_1, person_id_2)
  13  | delete_by_id                  | (records, person_id)
  14  | add_friend                    | (records, person_id, friend_id)
  15  | remove_friend                 | (records, person_id, friend_id)
  16  | add_education                 | (records, person_id, institute_name, ongoing, percentage)
----------------------------------------------------------------------------------------------------

For the logical cohesion of the program, you need to call function 1 first. Otherwise, there will be no entries for the program to work upon.
""")


    


def main():

    greetings()

    while True:

        func_key = int(input("\nEnter the value of the function you want to perform (A number from 1 to 16 can be entered): "))

        if func_key in range(1,17):

            if func_key == 1:

                records_local = read_data_from_file()

            elif func_key == 2:

                print(filter_by_first_name(records_local,input("\nfirst_name (STRING): The first name ")))

            elif func_key == 3:

                print(filter_by_last_name(records_local,input("\nlast_name (STRING): The last name ")))

            elif func_key == 4:

                print(filter_by_full_name(records_local,input("\nfull_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively) ")))

            elif func_key == 5:

                print(filter_by_age_range(records_local,int(input("\nmin_age (INTEGER): The minimum age (inclusive) ")),int(input("\nmax_age (INTEGER): The maximum age (inclusive) "))))

            elif func_key == 6:

                print(count_by_gender(records_local))

            elif func_key == 7:

                print('\naddress (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive) ')

                d = {}

                temp = input('\nEnter key "house_no", or leave it empty ')

                if temp != "":

                    d["house_no"] = int(temp)

                temp = input('\nEnter key "block", or leave it empty ')

                if temp != "":

                    d["block"] = temp

                temp = input('\nEnter key "town", or leave it empty ')

                if temp != "":

                    d["town"] = temp

                temp = input('\nEnter key "city", or leave it empty ')

                if temp != "":

                    d["city"] = temp

                temp = input('\nEnter key "state", or leave it empty ')

                if temp != "":

                    d["state"] = temp

                temp = input('\nEnter key "pincode", or leave it empty ')

                if temp != "":

                    d["pincode"] = int(temp)

                print(filter_by_address(records_local, d))

            elif func_key == 8:

                 print(find_alumni(records_local, input("\ninstitute_name (STRING): Name of the institute (case-insensitive) ")))

            elif func_key == 9:

                print(find_topper_of_each_institute(records_local))

            elif func_key == 10:

                print(find_blood_donors(records_local, int(input("\nreceiver_person_id (INTEGER): The ID of the donee "))))

            elif func_key == 11:

                print(get_common_friends(records_local, list(input("\nlist_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found. "))))

            elif func_key == 12:

                print(is_related(records_local, int(input("\nperson_id_1 (INTEGER): first person ID ")), int(input("\nperson_id_2 (INTEGER): second person ID "))))

            elif func_key == 13:

                records_local = delete_by_id(records_local, int(input("\nperson_id (INTEGER): The person id ")))

            elif func_key == 14:

                records_local = add_friend(records_local, int(input("\nperson_id (INTEGER): The person id ")), int(input("\nfriend_id (INTEGER): The friend id ")))

            elif func_key == 15:

                records_local = remove_friend(records_local, int(input("\nperson_id (INTEGER): The person id ")), int(input("\nfriend_id (INTEGER): The friend id ")))

            elif func_key == 16:

                percentage = 0

                person_id = int(input("\nperson_id (INTEGER): The person id "))

                inst_name = input("\ninstitute_name (STRING): The institute name (case-insensitive) ")

                boolean = input("\nongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not ")

                if boolean == "False":

                    percentage = input("\npercentage (FLOAT): The person's score in percentage ")

                if boolean == "True":

                    boolean = True

                if boolean == "False":

                    boolean = False

                records_local = add_education(records_local, person_id, inst_name, boolean, percentage)

            
        elif func_key == -1:

            break

        else:

            print("\nInvalid input! Try again.\n")

    print("\nThank you, and have a good day!\n")



    

if __name__ == "__main__":

    main()







