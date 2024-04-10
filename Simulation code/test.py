# Check if the chosen ID has data
if ID_chosen in all_vehicles_data and all_vehicles_data[ID_chosen]:
    # Get the number of records for the chosen vehicle
    num_records = len(all_vehicles_data[ID_chosen])
    # Iterate over each record of the chosen vehicle
    for i in range(num_records):
        chosen_vehicle_time = all_vehicles_data[ID_chosen][i].last_broadcast_time
        
        # Now iterate over other vehicles
        for vehicle_id, vehicle_movements in all_vehicles_data.items():
            # Check other vehicles with data
            if vehicle_id != ID_chosen and vehicle_movements:
                # Check if the current index i is within the range of other vehicle's records
                if i < len(vehicle_movements):
                    other_vehicle_time = vehicle_movements[i].last_broadcast_time
                    # Compare the times
                    if chosen_vehicle_time == other_vehicle_time:
                        print(chosen_vehicle_time)
                        #calculate the distance between my vehicle to the other vehicle
                        d = all_vehicles_data[ID_chosen][i].delta_t*c
                        if circumcirle_radius(all_vehicles_data[ID_chosen][i].dimension_x, all_vehicles_data[ID_chosen][i].dimension_y,1)\
                            +circumcirle_radius(vehicle_movements[i].dimension_x, vehicle_movements[i].dimension_y) > d:
                            print(f"Accident happened at time: {chosen_vehicle_time}")
                            
else:
    print(f"No data available for vehicle ID {ID_chosen}.")