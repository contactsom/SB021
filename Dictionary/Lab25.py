employeeDetails={
    1:"Kristina",
    2:"Sagar",
    3:"Michael",
    4:"Savita",
    5:"Sudipto",
    600:"Venkata"
    }

# If 600 as a key not present in dictionary employeeDetails, then take value as a "I am default Value"
# Where as, If present then take the actual value from the employeeDetails, which is "Venkata"
print(employeeDetails)
employeeDetails.setdefault(600,"I am default Value")
print(employeeDetails[600])
print(employeeDetails)
