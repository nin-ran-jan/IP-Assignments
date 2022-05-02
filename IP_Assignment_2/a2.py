# Assignment - 2
# Name - Niranjan Sundararajan
# Roll No - 2020090

import json



'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''




def read_data_from_file(file_path="data.json"):
    '''
    **** DO NOT modify this function ****
    Description: Reads the data.json file, and converts it into a dictionary.

    Parameters: 
    - file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

    Returns:
    - A dictionary containing the data read from the file
    '''
	
    with open(file_path, 'r') as data:
        
        records = json.load(data)

    return records


def filter_by_first_name(records, first_name):
    '''
    Description: Searches the records to find all persons with the given first name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - first_name (STRING): The first name

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given first name
	Case 1: No person found => Returns an empty list
	Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
	
    l = []
	
    for i in records:
                
        if i["first_name"].lower() == first_name.lower(): #Compared all characters in the strings by converting them to lower case as case-insensitive checking is required.

            l.append(i["id"])

    return l


def filter_by_last_name(records, last_name):
    '''
    Description: Searches the records to find all persons with the given last name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - last_name (STRING): The last name

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given last name
	Case 1: No person found => Returns an empty list
	Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''

    l = []
	
    for i in records:
                
        if i["last_name"].lower() == last_name.lower(): #Compared all characters in the strings by converting them to lower case as case-insensitive checking is required.

            l.append(i["id"])

    return l




def filter_by_full_name(records, full_name):
    '''
    Description: Searches the records to find all persons with the given full name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given full name
	Case 1: No person found => Returns an empty list
	Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''

    l = []
	
    for i in records:
                
        if i["first_name"].lower() + " " + i["last_name"].lower() == full_name.lower(): #Compared all characters in the strings by converting them to lower case as case-insensitive checking is required.

            l.append(i["id"])

    return l





def filter_by_age_range(records, min_age, max_age):
    '''
    Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - min_age (INTEGER): The minimum age (inclusive)
    - max_age (INTEGER): The maximum age (inclusive)

    Note: 0 < min_age <= max_age

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given age
	Case 1: No person found => Returns an empty list
	Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''

    l = []

    for i in records:
                
        if i["age"] in range(min_age, max_age+1): 

            l.append(i["id"])

    return l





def count_by_gender(records):
    '''
    Description: Counts the number of males and females

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A dictionary with the following two key-value pairs:
	KEY        VALUE
	"male"     No of males (INTEGER)
	"female"   No of females (INTEGER)
    '''

    m = 0
    f = 0

    for i in records: #A counter for loop, that increments the value of 1 to every entry of <m> and <f> as per the corresponding gender.
                
        if i["gender"] == "male": 

            m += 1

        elif i["gender"] == "female":

            f += 1

    return {"male":m,"female":f}





def filter_by_address(records, address):
    '''
    Description: Filters the person records whose address matches the given address. 

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
	Some examples are:
	    Case 1: {} 
		=> All records match this case
			
	    Case 2: { "block": "AD", "city": "Delhi" } 
		=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
	    Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

    Returns:
    - A LIST of DICTIONARIES with the following two key-value pairs:
	KEY            VALUE
	"first_name"   first name (STRING)
	"last_name"    last name (STRING)
    '''

    l = []
    c = 0 #counter

    for i in records:

        for j in address:

            if isinstance(address[j],str): #Checking if value is a string for case-insensitivity.
    
                if i["address"][j].lower() == address[j].lower(): #Compared all characters in the strings by converting them to lower case as case-insensitive checking is required.

                    c += 1

            else:

                if i["address"][j] == address[j]: #For values of type <int>

                    c += 1

        if c == len(address): #Will append to the list only if the length of the dictionary <address> is the same as c. This ensures all the subsets are printed for this condition.

            l.append({"first_name":i["first_name"],"last_name":i["last_name"]})

        c = 0 #Re-initialize the value of the counter for the following loops.

    return l

                


def find_alumni(records, institute_name):
    '''
    Description: Find all the alumni of the given institute name (case-insensitive). 
	
    Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - institute_name (STRING): Name of the institute (case-insensitive)

    Returns:
    - A LIST of DICTIONARIES with the following three key-value pairs:
	KEY            VALUE
	"first_name"   first name (STRING)
	"last_name"    last name (STRING)
	"percentage"   percentage (FLOAT)
    '''

    l = []

    for i in records:

        for j in range(len(i["education"])):

            if i["education"][j]["institute"].lower() == institute_name.lower() and i["education"][j]["ongoing"] == False: #The conditions is used for case-insensitivity.

                if j == len(i["education"])-1 or not(i["education"][j+1]["institute"].lower() == institute_name.lower() and i["education"][j+1]["ongoing"] == False):
                #This condition checks for the next iteration of the list. If the value corresponds to the current entry, the loop will not run for that entry. Therefore, if a person has multiple degrees from an institute, it will only append the entry with the highest index.
                    
                    l.append({"first_name":i["first_name"],"last_name":i["last_name"],"percentage": i["education"][j]["percentage"]})

    return l
        




def find_topper_of_each_institute(records):
    '''
    Description: Find topper of each institute

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

    Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
    '''

    d = {} #To be returned
    mark_checker = {} #To check the marks of the toppers of the institute.

    for i in records:

        for j in i["education"]:

            if j["ongoing"] == False:

                if j["institute"] not in d:

                    d[j["institute"]] = i["id"]
                    mark_checker[j["institute"]] = j["percentage"] #Initial entries are added irrespective of whether it corresponds to the entry of the topper.

                elif j["percentage"] > mark_checker[j["institute"]]: #To compare entries one by one and ultimately obtain the topper's results in the dictionary.

                    d[j["institute"]] = i["id"]
                    mark_checker[j["institute"]] = j["percentage"]

    return d
                
  

	


def find_blood_donors(records, receiver_person_id):
    '''
    Description: Find all donors who can donate blood to the person with the given receiver ID.

	Note: 
	- Possible blood groups are "A", "B", "AB" and "O".

	Rules:
	BLOOD GROUP      CAN DONATE TO
	A                A, AB
	B                B, AB
	AB               AB
	O                A, B, AB, O

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - receiver_person_id (INTEGER): The ID of the donee
	Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

    Returns:
    - A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
    '''
    
    rules = {"A":["A","O"],"B":["B","O"],"AB":["A","B","AB","O"],"O":["O"]} #To see which blood group a person can receive blood from.

    d = {}

    for i in records:

        if i["id"] == receiver_person_id:

            bg = i["blood_group"] #To obtain ID of the receiver.

            break

    for i in records:

        if i["blood_group"] in rules[bg] and i["id"] != receiver_person_id: #To see if the person is a viable donor or not.

            d[i["id"]] = i["contacts"]

    return d






def get_common_friends(records, list_of_ids):
    '''
    Description: Find the common friends of all the people with the given IDs

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

    Returns:
    - A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
    '''

    l = []

    for i in records: #0 145 5 04

        if i["id"] in list_of_ids:

            l = i["friend_ids"]

            break # l = 145

    for i in records:

        if i["id"] in list_of_ids:

            print(l)

            l = list(set(l) & set(i["friend_ids"]))#Uses set theory and obtains the intersection of the temporary sets in every iteration.

            print(l)

    return l



	


def is_related(records, person_id_1, person_id_2):
    '''
    **** BONUS QUESTION ****
    Description: Check if 2 persons are friends

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id_1 (INTEGER): first person ID
    - person_id_2 (INTEGER): second person ID

    Returns:
    - A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
    '''

    l = [person_id_1] #The list is used in the helper function and does not get re-initialized every time.

    def helper (records, person_id_1, person_id_2): #This function needs to be used in order to prevent the function from re-initializing the value of <l> after every recursive call.

        for i in records:

            if i["id"] == person_id_1:

                if person_id_2 in i["friend_ids"]:

                    return True #The <True> condition for a recursive program.

                else:

                    for j in i["friend_ids"]:

                        if j not in l:

                            l.append(j) #Appends to the list <l> to prevent the loop from being called multiple times and producing an infinite loop.

                            return helper(records, j, person_id_2)

        return False #Returns <False> if the friends are not common even after all the iterations.

    return helper (records, person_id_1, person_id_2) #Calling the helper function.


    	


def delete_by_id(records, person_id):
    '''
    Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
	
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''

    records_updated = records

    for i in records:

        if i["id"] == person_id:

            records_updated.remove(i)

    for j in records_updated: #Called the for loop twice as indexing can cause a problem if the record is deleted from the initial list <records>.

        if person_id in j["friend_ids"]:

            j["friend_ids"].remove(person_id)

    return records_updated

    


def add_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id
	
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''

    flag = 0

    for i in records:

        if i["id"] == person_id:

            flag += 1

        if i["id"] == friend_id:

            flag += 1

    if flag == 2:

        for i in records:

            if i["id"] == person_id and friend_id not in i["friend_ids"]: #Can only add a frined if a person does not already have the friend to start with.

                i["friend_ids"].append(friend_id)

            if i["id"] == friend_id and person_id not in i["friend_ids"]: #Can only add a frined if a person does not already have the friend to start with.

                i["friend_ids"].append(person_id)

    return records



	


def remove_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id
	
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    	
    flag = 0

    for i in records:

        if i["id"] == person_id:

            flag += 1

        if i["id"] == friend_id:

            flag += 1

    if flag == 2:

        for i in records:

            if i["id"] == person_id and friend_id in i["friend_ids"]: #Can only remove the friend if they are there to begin with.

                i["friend_ids"].remove(friend_id)

            if i["id"] == friend_id and person_id in i["friend_ids"]: #Can only remove the friend if they are there to begin with.

                i["friend_ids"].remove(person_id)

    return records



    

def add_education(records, person_id, institute_name, ongoing, percentage):
    '''
    Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - institute_name (STRING): The institute name (case-insensitive)
    - ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
    - percentage (FLOAT): The person's score in percentage

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
	
    for i in records:

        if i["id"] == person_id:

            if ongoing == True: #Checks whether the individual has completed the education in an institution or not.

                i["education"].append({"institute":institute_name.upper(), "ongoing":True})

            elif ongoing == False:

                i["education"].append({"institute":institute_name.upper(), "ongoing":False, "percentage":percentage})

    return records      
