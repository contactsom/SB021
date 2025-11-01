employeeDetails={
    1:"Kristina",
    2:"Sagar",
    3:"Michael",
    4:"Savita",
    5:"Sudipto"
    }

print(employeeDetails)
employeeDetails.setdefault(600,"I am default Value")
print(employeeDetails[600])
print(employeeDetails)
