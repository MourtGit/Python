""" This program prints out the last name of the second employee by searching through the dictionary below"""

d = {"employees" : [{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna","lastName":"Smith"},
                    {"firstName":"Peter","lastName":"Jones"}],
    "owners":[{"firstName":"Jack","lastName":"Petter"},{"firstName":"Jessy","lastName":"Petter"}]}

last_name=d["employees"][1]["lastName"]
print(last_name)

# empl_list=d["employees"] # list of employees
# second_empl=empl_list[1] # second employee dictionary
# last_name=second_empl["lastName"] # value of key 'lastName'
