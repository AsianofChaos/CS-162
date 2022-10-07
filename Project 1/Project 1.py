class engine:
    def __init__(
        self, 
        num_pistons, 
        displacement, 
        piston_layout, 
        cam_layout):

        self.num_pistons = num_pistons
        self.displacement = displacement
        self.piston_layout = piston_layout
        self.cam_layout = cam_layout



    def __str__(self):
        pass
    
    def indv_piston_diplacement(self):
        
        indv_piston_diplacement = int(self.displacement) / int(self.num_pistons)

        return indv_piston_diplacement



test = engine

user_input = None
first_run = None
while user_input != "1":
#user input
    invalid_input = True
    while invalid_input == True:
        user_input = input(
            "1: Quit\n" \
            "2: \n" \
            "2: \n" \
            "Enter Input:"
        )
        if user_input not in ["1", "2", "3"]:
            print("Invalid input")
        else:
            invalid_input = False 


    #runs requested input
    if first_run:
        pass
    if user_input == "1":
        pass
    elif user_input == "2":
        plcholder = input(f"plcholder input:")
    elif user_input == "2":
        pass
        #break
    first_run = False

print("Goodnight")






