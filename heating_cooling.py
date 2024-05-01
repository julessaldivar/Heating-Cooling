def heating_cooling():  # defining function
    outcome = actual_temp - desired_temp  # used to compare values
    if outcome > 0:
        return 'Run A/C'
    if outcome < 0:
        return 'Run Heat'
    else:
        return 'Standby'


actual_temp = int(input("What's the current temperature?: "))
desired_temp = int(input("What's the desired temperature?: "))
print(heating_cooling())  # printing execution of function
