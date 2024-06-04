from random import expovariate

class Customer:
    def __init__(self, id_num, arrival_time):
        self.__idNum = id_num
        self.__arrivalTime = arrival_time

    def get_id(self):
        return self.__idNum

    def get_arrival_time(self):
        return self.__arrivalTime
    
    def __str__(self):
        return f"Customer {self.__idNum}"

class Server:
    def __init__(self):
        self.__customer = None
        self.__stopTime = None

    def start_service(self, customer, stop_time):
        self.__customer = customer
        self.__stopTime = stop_time

    def stop_service(self):
        customer = self.__customer
        self.__customer = None
        return customer

    def get_stop_time(self):
        return self.__stopTime

    def is_free(self):
        return self.__customer is None

class Simulation:
    def __init__(self, lamda, mu, total_time):
        self.__lamda = lamda
        self.__mu = mu
        self.__total_time = total_time
        self.__customer_queue = []
        self.__total_wait_time = 0
        self.__num_customers = 0
        self.server = Server()

    def run(self):
        current_time = 0
        next_arrival = round(expovariate(self.__lamda))
        print(f"arTime: {next_arrival} current time: {current_time}")

        while current_time < self.__total_time:
            print(f"current time: {current_time}")
            print([str(customer) for customer in self.__customer_queue])

            if not self.server.is_free() and current_time >= self.server.get_stop_time():
                served_customer = self.server.stop_service()
                self.__total_wait_time += current_time - served_customer.get_arrival_time()

            if self.__customer_queue and self.server.is_free():
                customer = self.__customer_queue.pop(0)
                service_time = round(expovariate(self.__mu))
                print(f"serTime: {service_time} current time: {current_time}")
                self.server.start_service(customer, current_time + service_time)

            if current_time >= next_arrival:
                new_customer = Customer(self.__num_customers + 1, next_arrival)
                self.__customer_queue.append(new_customer)
                self.__num_customers += 1
                print(f"arTime: {next_arrival} current time: {current_time}")
                next_arrival = current_time + round(expovariate(self.__lamda))

            current_time += 1  # Increment time

    def get_average_wait_time(self):
        return self.__total_wait_time / self.__num_customers if self.__num_customers > 0 else 0

    def get_queue_length(self):
        return len(self.__customer_queue)
    
def calculate_theoretical_values(lamda, mu):
    if mu <= lamda:
        raise ValueError("System is unstable (mu must be greater than lambda)")

    rho = lamda / mu  # Utilization factor
    L = rho / (1 - rho)  # Average number of customers in the system
    W = 1 / (mu - lamda)  # Average time a customer spends in the system
    L_q = (lamda ** 2) / (mu * (mu - lamda))  # Average number of customers in the queue
    W_q = W - (1 / mu)  # Average time a customer spends waiting in the queue

    return L, W, L_q, W_q


def main():
    lamda = 2  # Arrival rate
    mu = 10    # Service rate
    total_time = 600  # Simulation time in minutes

    simulation = Simulation(lamda, mu, total_time)
    simulation.run()

    print("Average waiting time:", simulation.get_average_wait_time())
    print("Length of the queue at the end:", simulation.get_queue_length())
    
    L, W, L_q, W_q = calculate_theoretical_values(lamda, mu)
    print(f"Average number of customers in the system (L): {L}")
    print(f"Average time a customer spends in the system (W): {W}")
    print(f"Average number of customers in the queue (L_q): {L_q}")
    print(f"Average time a customer spends waiting in the queue (W_q): {W_q}")



if __name__ == "__main__":
    main()
