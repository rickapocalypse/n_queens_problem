import models.model as m
import helpers
import random 

class StochasticHillClimbing(m.Model):
    def indice(n):
        for num in range(0,n):
            return num


    def move_next(self):
        super().move_next()
        state_is_goal = False
        cost_current_state = len(helpers.find_attacking_pairs(self.state))
        for n in range(0,7):

            next_state = self.state.copy()
            next_state[n] = random.randrange(0,7)
            cost_next_state = len(helpers.find_attacking_pairs(next_state))
            dE = cost_next_state - cost_current_state

            if dE < 0:
                self.state = next_state
                break

