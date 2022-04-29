import models.model as m
import helpers
import random
import math

class my_hill(m.Model):
    indice = 0
    t = 100


    def move_next(self):
        super().move_next()
        cost_current_state = len(helpers.find_attacking_pairs(self.state))
        state_is_goal = False 
        
        while state_is_goal != True:
#============== Estados ==============#            
            next_state0 = self.state.copy()
            next_state1 = self.state.copy()
            next_state2 = self.state.copy()
            next_state3 = self.state.copy()
            next_state4 = self.state.copy()
            next_state5 = self.state.copy()
            next_state6 = self.state.copy()
            next_state7 = self.state.copy()
#============== Mudança de cada estado aleatorio ==============#
            next_state0[0] = random.randrange(0,7)
            next_state1[1] = random.randrange(0,7)
            next_state2[2] = random.randrange(0,7)
            next_state3[3] = random.randrange(0,7)
            next_state4[4] = random.randrange(0,7)
            next_state5[5] = random.randrange(0,7)
            next_state6[6] = random.randrange(0,7)
            next_state7[7] = random.randrange(0,7)
#============== Custo ==============#
            cost0 = len(helpers.find_attacking_pairs(next_state0))
            cost1 = len(helpers.find_attacking_pairs(next_state1))
            cost2 = len(helpers.find_attacking_pairs(next_state2))
            cost3 = len(helpers.find_attacking_pairs(next_state3))
            cost4 = len(helpers.find_attacking_pairs(next_state4))
            cost5 = len(helpers.find_attacking_pairs(next_state5))
            cost6 = len(helpers.find_attacking_pairs(next_state6))
            cost7 = len(helpers.find_attacking_pairs(next_state7))
#============== Conjunto chave e valor de estados e custo ==============#
            d = {'0': cost0,'1': cost1,'2': cost2,'3': cost3,'4': cost4, '5': cost5,'6': cost6, '7':cost7}
#============== Selecionando os estados correspondente ao menor valor ==============#

            minval = min(d.values())
            res = [k for k, v in d.items() if v==minval]
            choice = random.choice(res)
            
            if choice == '0':
                next_state = next_state0
                cost = d['0']
                
            if choice == '1':
                next_state = next_state1
                cost = d['1']
            if choice == '2':
                next_state = next_state2
                cost = d['2']
            if choice == '3':
                next_state = next_state3
                cost = d['3']
            if choice == '4':
                next_state = next_state4
                cost = d['4']
            if choice == '5':
                next_state = next_state5
                cost = d['5']
            if choice == '6':
                next_state = next_state6
                cost = d['6']
            if choice == '7':
                next_state = next_state7
                cost = d['7']
            """if self.indice > 7:
                v = []
                for n in range(0,8):
                    v.append(random.randrange(0,7))
                print(v)
                self.indice = 0
                self.state = v
                break
"""

            if cost < cost_current_state:
                self.state = next_state
                break
            else:
                self.indice += 1
            if self.indice > 8:
                break


                



