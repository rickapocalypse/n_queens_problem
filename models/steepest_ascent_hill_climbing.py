import models.model as m
import helpers

class SteepestAscentHillClimbing(m.Model):
    def move_next(self):
        super().move_next()
        state_cost = len(helpers.find_attacking_pairs(self.state)) 

        for next_state in helpers.generate_next_states(self.state):
            for cost in helpers.evaluate_next_states(next_state):
                if min(cost) < state_cost:
                    if len(helpers.find_attacking_pairs(next_state)) < state_cost:
                        self.state = next_state
                        break