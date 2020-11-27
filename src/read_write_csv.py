import csv 

#Read a CSV ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#!!! Creta the given file first !!!
with open("software.csv") as software:
    #Command user to read as a dictionary
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))
        
        
#Write into a CSV +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
#Declares a list of dictionaries        
users = [{"name":"Sol Mansi", "username":"solm", "department":"IT infrastructure"}, 
{"name":"Lio Nelson", "username":"lion", "department":"User Experience Research"}, 
{"name":"Charly Grey", "username":"greyc", "department":"Development"}]

#It cretaes a list in order to have he keys in order to make a comparison
keys = ["name", "username", "department"]

#writes inside the csv file. Including the headers and the rows, as it were a table.
with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)