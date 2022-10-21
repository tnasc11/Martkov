from customer import Customer
from supermarket import Supermarket

simulation_time = 60 * 15  ## run simulation for 15 hours

def start_simulation():
    s = Supermarket.Supermarket()
    for i in range(simulation_time):
        s.get_time()
        s.print_customers()
        s.add_new_customers()
        s.next_minute()
        s.remove_finished_customers()
