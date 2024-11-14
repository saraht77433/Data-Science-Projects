# DSC510
# Programming Assignment Week 6
# Sarah Theriot
# 7/9/2024

# Define functions to get input from user.


def get_temperatures():
    temperatures = []
    while True:
        temp_list = input("Enter a temperature (or 'Done' when finished): ")
        if temp_list == 'Done':
            break
        try:
            temperature = float(temp_list)
            temperatures.append(temperature)
        except ValueError:
            print("Please enter a valid temperature or 'Done' when finished.")
    return temperatures


def largest_temperature(temperatures):
    if temperatures:
        return max(temperatures)
    else:
        return None


def smallest_temperature(temperatures):
    if temperatures:
        return min(temperatures)
    else:
        return None


def main():
    temperatures = get_temperatures()

    if temperatures:
        largest_temp = largest_temperature(temperatures)
        smallest_temp = smallest_temperature(temperatures)

        print("Largest Temperature: ", largest_temp)
        print("Smallest Temperature: ", smallest_temp)
        print("Number of temperatures: ", len(temperatures))

    else:
        print("No temperatures entered.")


if __name__ == "__main__":
    main()
