import os
import time 
import random
import scipy.stats
import numpy as np

from ..operator import operator as opt

EPS = 1e-6

class SHADE(object):

    def __init__(self):
        # params
        self.pop_size = None
        self.gen_size = None
        self.memory_size = None
        self.archive_size = None

        # problem related params
        self.dim = None
        self.lb = None
        self.ub = None

        # population
        self.pop = None
        self.fit = None
        
        # states
        self.m_cr = None
        self.m_f = None
        self.archive = None
        self.k = None

        # load default params
        self.set_params(self.default_params())

    def default_params(self, benchmark=None):
        params = {}
        params['pop_size'] = 300
        params['memory_size'] = 6

        # define the archive size
        params['archive_size']=200 
        
        return params

    def set_params(self, params):
        for param in params:
            setattr(self, param, params[param])

    def optimize(self, evaluator):
        self.init(evaluator)

        memory_idxes = list(range(self.memory_size))
        while not evaluator.terminate():

            # adaptation parameter generation
            r = np.random.choice(memory_idxes, self.pop_size)
            cr = np.random.normal(self.m_cr[r], 0.1, self.pop_size)
            cr = np.clip(cr, 0, 1)
            cr[cr == 1] = 0
            f = scipy.stats.cauchy.rvs(loc=self.m_f[r], scale=0.1, size=self.pop_size)
            f[f>1] = 0
            
            while sum(f<=0) != 0:
                r = np.random.choice(memory_idxes, sum(f<=0))
                f[f<=0] = scipy.stats.cauchy.rvs(loc=self.m_f[r], scale=0.1, size=sum(f <= 0))

            # parameter of pbest
            p = np.random.uniform(low=2/self.pop_size, high=0.2, size=self.pop_size)
        
            # Common Steps
            mutated = opt.current_to_pbest_mutation(self.pop, self.fit, f.reshape(len(f), 1), p, archive=self.archive)
            crossed = opt.crossover(self.pop, mutated, cr.reshape(len(f), 1))

            c_fit = evaluator(crossed)

            # Selection
            # Here index indicate the eliminated individuals, or improved individuals
            self.pop, indexes = opt.paired_select(self.pop, self.fit, crossed, c_fit, return_indexes=True)

            # Adapt for new generation
            self.archive.extend(self.pop[indexes])
            
            if len(indexes) > 0:
                if len(self.archive) > self.archive_size:
                    self.archive = random.sample(self.archive, self.archive_size)
                if max(cr) != 0:
                    weights = np.abs(self.fit[indexes] - c_fit[indexes])
                    weights /= np.sum(weights)
                    self.m_cr[self.k] = np.sum(weights * cr[indexes])
                else:
                    self.m_cr[self.k] = 1
                
                self.m_f[self.k] = np.sum(f[indexes]**2)/np.sum(f[indexes])

                self.k += 1
                if self.k == self.memory_size:
                    self.k = 0

                self.fit[indexes] = c_fit[indexes]

        return evaluator.best_y, evaluator.obj.optimal_val

    def init(self, evaluator):

        # record problem related params
        self.dim = opt.dim = evaluator.obj.dim
        self.lb = opt.lb = evaluator.obj.lb
        self.ub = opt.ub = evaluator.obj.ub

        # init random seed
        self.seed = int(os.getpid()*time.time() % 1e8)
        np.random.seed(self.seed)
        random.seed(self.seed)

        # init pop
        self.pop = np.random.uniform(self.lb, self.ub, [self.pop_size, self.dim])
        self.fit = evaluator(self.pop)

        # inti states
        self.m_cr = np.ones(self.memory_size) * 0.5
        self.m_f = np.ones(self.memory_size) * 0.5
        self.archive = []
        self.k = 0