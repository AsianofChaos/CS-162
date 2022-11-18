class car:
    def __init__(
        self,
        new_name = "no name given",
        new_make = "Honda",
        new_model = "Civic",
        new_engine_horsepower = 158,
        new_engine_displacement = 2.0,
        new_engine_displacement_unit = "L",
        new_engine_number_pistons = 4,
        new_transmission = "Automatic CVT",
        new_ignition_on = False
        ): 

        self.name = new_name
        self.make = new_make
        self.model = new_model
        self.power = new_engine_horsepower
        self.displacement = new_engine_displacement
        self.displacement_unit = new_engine_displacement_unit
        self.num_pistons = new_engine_number_pistons
        self.transmission = new_transmission
        self.ignition_on = new_ignition_on
    
    
    def toggle_ignition(self):
        self.ignition_on = not self.ignition_on


    def __str__(self):
        if self.ignition_on == False:
            result = "The car is off."
        else:
            result = f"self.name: {self.name}:\n" \
            f"\tself.make: {self.make}\n" \
            f"\tself.model: {self.model}\n" \
            f"\tself.power: {self.power}\n" \
            f"\tself.displacement: {self.displacement}\n" \
            f"\tself.displacement_unit: {self.displacement_unit}\n" \
            f"\tself.num_pistons: {self.num_pistons}\n" \
            f"\tself.transmission: {self.transmission}\n" \
            f"\tself.ingnition_on: {self.ignition_on}" 
        return result 

    def indv_piston_diplacement(self):
        
        indv_piston_diplacement = int(self.displacement) / int(self.num_pistons)

        return indv_piston_diplacement





user_input = "-1"
first_run = True
while user_input != "0":
#user input menu display
    invalid_input = True
    while invalid_input == True:
        user_input = input(
            "0: Quit\n" \
            "1: Input vehical specifications\n" \
            "2: Display vehical specifications\n" \
            "3: toggle ingition power\n" \
            "Enter Input:"
        )
        if user_input not in ["0", "1", "2", "3"]:
            print("Invalid input")
        else:
            invalid_input = False 


    #runs requested input
    if first_run:
        my_car = None

    if user_input == "1":
        new_vehicle_name = input(f"What is the name of the car\n")
        new_car_make = input(f"\nWhat is the make of the car?\n")
        new_car_model = input(f"\nWhat is the model of the car?\n")
        
        my_car = car(new_vehicle_name, new_car_make, new_car_model)

    elif user_input == "2":
        if my_car == None:
            print("No car exists.")
        else:
            print(my_car)

    elif user_input == "3":
        if my_car != None:
            my_car.toggle_ignition()
            if my_car.ignition_on:
                print("Ignition on.")
            else:
                print("Ignition off.")
        else:
            print("no car exits")
    #quit
    elif user_input == "0":
        pass

        
    first_run = False

print("end")






