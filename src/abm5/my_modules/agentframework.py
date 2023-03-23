



import random
import geometry

#random.seed(0)
class Agent:
    def __init__(self, i, environment, n_rows, n_cols):
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
        self.i = i
        self.environment = environment
        tnc = int(n_cols / 3)
        self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        tnr = int(n_rows / 3)
        self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        self.store = 0
        
    
        
    def eat(self):
       
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def share(self, neighbourhood):
        """
        share the store in the range of neighbourhood

        Parameters
        ----------
        neighbourhood : list
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
        
    def __str__(self):
        return self.__class__.__name__ + "(i="+str(self.i)+" ,x=" + str(self.x) + ", y=" + str(self.y) + ")"
    
    def __repr__(self):
        return str(self)
    
    def move(self, x_min, y_min, x_max, y_max):
        #move randomly
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
                
            
        
        
        
        
                
        
        
   
                     
            
         