'''car class'''


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
        new_transmission = "Automatic",
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




