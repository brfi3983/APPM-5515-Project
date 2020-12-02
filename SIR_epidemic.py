import numpy as np
import numpy.random as rand

# A is the adjacency matrix as a numpy array.
# Vaccination not yet implemented
class SIR_class():
    def __init__(self, A):
        self.A = A
        self.n = A.shape[0]

    def SIR(beta, mu, delta_t, T, v_0, vaccinated = False):
        # Initialize variables
        num_timesteps = T/delta_t
        q = mu * delta_t
        p = beta * delta_t

        susceptible_nodes = np.r_[0:(self.A.shape[0] - 1):1] # all nodes susceptible at first
        susceptible_nodes.remove(v_0)   # remove first infected

        infectious_nodes = [rand.randint(0, self.n-1)]
        recovered_nodes = np.empty(0)

        # Main loop
        for t in (1,num_timesteps):
            for v in infectious_nodes:
                # Neighbors of v become infected with probability p
                for s in susceptible_nodes:
                    if self.A[v,s].equals(1):
                        r = rand.uniform(0,1)
                        if r > p:
                            infectious_nodes.append(s)
                            susceptible_nodes.remove(s)
                r = rand.uniform(0,1)
                if r > q:
                    recovered_nodes.append(v)
                    infectious_nodes.remove(v)

        return [susceptible_nodes, infectious_nodes, recovered_nodes]








