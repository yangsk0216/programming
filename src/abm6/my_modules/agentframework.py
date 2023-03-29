import my_modules.geometry as geometry
import random

random.seed(3)
class Agent:
    def __init__(self, agents, i, environment, n_rows, n_cols):
        """
        The constructor method.

        Parameters
        ----------
        agents : List
            A list of Agent instances.
            i : Integer
            To be unique to each instance.
            environment : List
            A reference to a shared environment
            n_rows : Integer
            The number of rows in environment.
            n_cols : Integer
        The number of columns in environment.

        Returns
        -------
        None.

        """
        self.agents = agents
        self.i = i
        self.environment = environment
        tnc = int(n_cols / 3)
        self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        tnr = int(n_rows / 3)
        self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        #Create some more variable results by randomly setting the store of each agent in initialisation to be a value between 0 and 99.
        self.store = random.randint(0,99)
        self.store_shares = 0
        
        #
    def share(self, neighbourhood):
        """
        share the store in the range of neighbourhood

        Parameters
        ----------
        neighbourhood : Number
            Distance Threshold

        Returns
        -------
        None.

        """
        # Create a list of agents in neighbourhood
        neighbours = []
        #print(self.agents[self.i])
        for a in self.agents:
            distance = geometry.get_distance(a.x, a.y, self.x, self.y)
            if distance < neighbourhood:
                neighbours.append(a.i)
        # Calculate amount to share
        n_neighbours = len(neighbours)
        #print("n_neighbours", n_neighbours)
        shares = self.store / n_neighbours  
        #print("shares", shares)
        # Add shares to store_shares
        for i in neighbours:
            self.agents[i].store_shares += shares
            
            
        
    def eat(self):
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        if self.store > 100:
            #Change the eat function so that if an agent store goes above 100, then half the store is released back to the environment at the agent's location.
            self.environment[self.y][self.x] += self.store/2
            self.store -= self.store/2
            
    
    def __str__(self):
        return self.__class__.__name__ + "(i="+str(self.i)+" ,x=" + str(self.x) + ", y=" + str(self.y) + ")"
    
    def __repr__(self):
        return str(self)
    
    def move(self, x_min, y_min, x_max, y_max):
        ##move randomly
        rn = random.random()
        if rn < 0.5:
            self.x =  self.x + 1
        else:
            self.x =  self.x - 1

        rn = random.random()
        if rn < 0.5:
            self.y =  self.y + 1
        else:
            self.y =  self.y - 1
        # Apply movement constraints.
        if self.x < x_min:
             self.x = x_min
        if  self.y < y_min:
             self.y = y_min
        if self.x > x_max:
             self.x = x_max
        if self.y  > y_max:
             self.y  = y_max
                
def sum_environment(environment):
    """
    sum the value of the environement

    Parameters
    ----------
    environment : list
        basemap.

    Returns
    -------
    sum_environment : Number
        The sum of all values in the environment

    """
    #Traversing arrays
    sum_environment = 0
    for i in range(len(environment)):
        for j in range(len(environment[i])):
            sum_environment += environment[i][j]
    return sum_environment

def sum_agent_stores(agents):
    """
    sum the value of the environement that stored

    Parameters
    ----------
    agents : LIST
        List  stored coordinates

    Returns
    -------
    sum_agent_stores : Number
        The sum of all values in the environment that stored

    """
    sum_agent_stores = 0
    for i in range(len(agents)):
        sum_agent_stores += agents[i].store
    return sum_agent_stores
      
           
        
        
        
        
                
        
        
   
                     
            
         