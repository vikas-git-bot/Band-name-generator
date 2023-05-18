for i in range(4):
    # 1. create a greeting for your program
    print('''Welcome to The band name Generator.!!! \n''')

    # 2. Ask the user for thr city that they grew up in.
    name_of_city = input("Name of the city you grew up in? \n").title()

    # 3. Ask the user for the name of the pet.
    name_of_pet = input("What is the name of your pet? \n").title()

    # 4. Combine the name of their city and pet and show them their band name
    print(f"Your Band Name could be {name_of_city} {name_of_pet}")

