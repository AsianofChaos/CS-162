'''Menu for Car'''
import Car


def main():

    # menu
    user_input = "-1"
    first_run = True
    while user_input != "0":
    # user input menu display
        invalid_input = True
        while invalid_input == True:
            user_input = input(
                "0: Quit\n" \
                "1: Input vehical specifications\n" \
                "2: Display vehical specifications\n" \
                "3: toggle ingition power\n" \
                "4: Save to file\n" \
                "5: Read from file\n" \
                "Enter Input:"
            )
            if user_input not in ["0", "1", "2", "3", "4", "5"]:
                print("Invalid input")
            else:
                invalid_input = False 

        # runs requested input
        if first_run:
            my_car = None

        if user_input == "1":
            
            try:
                new_car_name = input(f"What is the name of the car\n")
                new_car_make = input(f"\nWhat is the make of the car?\n")
                new_car_model = input(f"\nWhat is the model of the car?\n")
            
                new_car_power = int(input(f"\nWhat is the horsepower of the car engine?\n"))
            
                my_car = Car.car(new_car_name, new_car_make, new_car_model, new_car_power)
            
                isinstance(new_car_power, int)
            except:
                print("input the correct datatype.")
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
        # quit
        elif user_input == "4":
            # Writes the currect opject values to a file
            try:
                with open("Car.txt", "w") as output_file:
                    output_file.write(f"{my_car}")
            except:
                print("error")
        elif user_input == "5":
            # Reades the object values from a file
            try:
                with open("Car.txt", "r") as input_file:
                    raw_inputs = input_file.readlines()
                    for line in raw_inputs:
                        splitline = line.split(": ")
                        print(f"split_line: {splitline}")
                    #print(raw_input)



            except FileNotFoundError as fnfe:
                print("No file found.")
        
        
        elif user_input == "0":
            pass

            
        first_run = False

    print("end")


if __name__ == "__main__":
    print(f"__name__ in my menu file: {__name__}")
    main()



