import random
### how to use
# create handler
# add handler to drone
#
#
# after completing previous steps for all drones, run on one of them .handle_token
###

class pos_handler:
    id = -1
    list_of_drones = []
    current_table = None #TODO

    def __init__(self, list_of_drones):
        self.configure(list_of_drones)
        print('constructor for: ' + str(self.id))

    def set_list_of_drones(self, drones):
        self.list_of_drones = drones

    def pass_token(self):
        #TODO
        drone = random.choice(self.list_of_drones)
        drone.handle_token()
        print('TODO')

    def find_id(self, drones):
        self.id = len(drones)

    def send_table_broadcast(self):
        #TODO
        print('Table sent to all')
        for drone in self.list_of_drones:
            self.send_table(drone)
        self.pass_token()

    def send_table(self, drone):
        print('Table sent')

    def handle_token(self):
        print('handle')
        #to show that something happens here
        x = input('Pass token')
        print('Token handle in drone: ' + str(self.id) )
        #==========
        self.send_table_broadcast()
        self.pass_token()

    def configure(self, list_of_drones):
        print('configure')
        self.set_list_of_drones(list_of_drones)
        self.find_id(list_of_drones)

