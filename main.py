# This program is for the company AutoCountry
# CarFinder program

# Vehicle list
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Print menu
def printMenu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print()
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit") 

printMenu() 

# Input
enteredNum = int(input())
if enteredNum == 1:
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList: 
        print(vehicle)
    printMenu()

elif enteredNum == 2:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
