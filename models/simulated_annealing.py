import models.model as m
import helpers
import random
import math

class SimulatedAnnealing(m.Model):
    def __init__(self):
        self.T = 100
        print(f'T inicial: {self.T}')
        self.index = 0
        super()

    def checkTemperature(self):
        return False if self.T == 0 else True

    def setNewTemperatura(self):
        self.T = self.T - 1

    def callBack(self, row, column):
        pass

    def move_next(self):
        super().move_next()
        #self.setNewTemperatura()
        #print(f'T novo: {self.T}')
        
        self.T *= 0.99
        state_cost = len(helpers.find_attacking_pairs(self.state))
        while self.T > 0:

            random_state = self.state.copy()
            self.index = random.randrange(0,7)
            random_state[self.index] = random.randrange(0,7)
            cost_random_state = len(helpers.find_attacking_pairs(random_state))
            
            dE = cost_random_state - state_cost
            print(self.T)
            print(dE)
            prob = math.exp( -(dE / self.T))
    
            if cost_random_state == 0 or state_cost == 0:
                print('solução encontrada')

            if dE < 0 or random.uniform(0,1) < prob:
                self.state = random_state.copy()
                break


  
           




"""



        state_cost = len(helpers.find_attacking_pairs(self.state))
        print(self.index)
        while self.T != 0:
            random_state = self.state.copy()
            random_state[self.index] = random.randrange(0,7)
            random_state_cost = len(helpers.find_attacking_pairs(random_state)) 

            if random_state_cost < state_cost:
                self.state = random_state
                self.index += 1
                break





===========================

        state_cost = len(helpers.find_attacking_pairs(self.state))

        for next_state in helpers.generate_next_states(self.state):
            random_state = next_state.copy()
            self.index = random.randrange(0,7)            

            random_state[self.index] = random.randrange(0,7)
            print(random_state)
            print(self.state)
            random_state_cost = len(helpers.find_attacking_pairs(random_state))
            
           
            
            de = random_state_cost - state_cost
            
            if self.T == 0:
                return self.state
                break
            

            if de <= 0:
                self.state = random_state
                #self.index += 1
                break
            else:
                if random.random() < de:
                    self.state = random_state
                #self.index += 1
                break

"""
