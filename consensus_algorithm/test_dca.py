import drone_consensuse_algorithm as cons

list_of_drones = []
drone1 = cons.pos_handler(list_of_drones)
list_of_drones.append(drone1)
drone2 = cons.pos_handler(list_of_drones)
list_of_drones.append(drone2)
drone3 = cons.pos_handler(list_of_drones)
list_of_drones.append(drone3)

list_of_drones[0].handle_token()


