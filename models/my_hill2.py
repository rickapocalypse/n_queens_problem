import models.model as m
import helpers
import random
import math

class my_hill2(m.Model):
    indice = 0
    t = 100


    def move_next(self):
        super().move_next()
        self.t *= 0.9
        cost_current_state = len(helpers.find_attacking_pairs(self.state))
        print(self.t)

        for next_state in helpers.generate_next_states(self.state):
            next_state_cost = len(helpers.find_attacking_pairs(next_state))
            dE = next_state_cost - cost_current_state
            prob = math.exp( -(dE / self.t))

            if dE < 0 or random.uniform(0,1) > prob:
                self.state = next_state.copy()
                break


            
            
        
        