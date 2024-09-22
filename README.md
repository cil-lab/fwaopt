# FWAOPT: Multi-Population Optimization Based on Fireworks Algorithm

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

`fwaopt` is a flexible framework for complex optimization tasks by managing multiple populations.

> **Note:** We only consider **Bound-Constrained**, **Continuous**, **Black-Box**, **Minimization** optimization problems.

This repository is a generalized framework of **Fireworks Algorithm** and traditional [EA](#definitions)s and [SIOA](#definitions)s. It is inspired from the research of ([FWA](https://www.cil.pku.edu.cn/fwa/index.htm)) and presently mainly used in FWA-related research and applications.

The repository contains:

1. Basic operators used in EAs and SIOAs.

2. Methods and examples for designing populations.

3. Methods and examples for designing optimization algorithms with population.

4. A new objective function interface and some pre-compiled benchmarks.

5. Analysis tools for optimization results.

## Table of Contents

- [Sections](#sections)
  - [Background](#background)
  - [Install](#install)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
- [Definitions](#definitions)

## Background

`mpopt` is motivated by the research of [FWA](https://link.springer.com/content/pdf/10.1007/978-3-642-13495-1_44.pdf), in which multiple population called fireworks are maintained for optimization. This optimization framework is of great significance in future research and application. The aim of this repository is to provide a complete set of toolkits for designing, benchmarking and applying those methods.

The latest information on FWA can be found at [here](https://www.cil.pku.edu.cn/fwa/index.htm).

## Install

To install 'mpopt', run the following commands:

```sh
git clone https://github.com/cil-lab/fwaopt.git
cd mpopt
python3 setup.py install
```

If you do not have the super authority, run `python3 setup.py install --user` instead.

> Note: 'numpy' is required for this repository.

## Usage

Here, we illustrate how to optimize using `mpopt`. First of all, `numpy` is needed in most parts of the package.

```python
import numpy as np
```

### Objective Function

If you want to provide a handcraft objective, a callable function is needed first. For example:

```python
def my_func(X):
    return np.sum(X**2)
```

Then, an `ObjFunction` instance should be created using the callable function with some additional infomation, which illustrate how the function should be called:

```python
from mpopt.tools.objective import ObjFunction
obj = ObjFunction(my_func, dim=2, lb=-1, ub=1)
```

`ObjFunction` instance can be called directly, but it is better to create a `Evaluator` instance for each run of optimization. 

```python
from mpopt.tools.objective import Evaluator
evaluator = Evaluator(obj, max_eval = 100)
```

You can also get a evaluator from provided benchmark easily:

(Note: All benchmarks are written in C language, so they need to be compiled before running. For the compilation instruction, please refer to [mpopt/benchmarks/readme.md](./mpopt/benchmarks/readme.md))

```python
from mpopt.benchmarks.benchmark import Benchmark
# get CEC20 benchmark in 10 dimension.
benchmark = Benchmark('CEC20', 10)
# get a evaluator for the first function
func_id = 0
evaluator = benchmark.generate(func_id)
```

The evaluator holds the setting of optimization task and record states during the optimization. For example, a random search can simply be completed by following code:

```python
lb = evaluator.obj.lb
ub = evaluator.obj.ub
dim = evaluator.obj.dim
sample_num = 10
while not evaluator.terminate():
    rand_samples = np.random.uniform(lb, ub, [sample_num, dim])
    fitness = evaluator(rand_samples)
print("Optimal: {}, Value: {}.".format(evaluator.best_x, evaluator.best_y))
```

### Algorithm

Currently, `mpopt` provie some classic population based algorithms which can be used directly. We are planning on providing a lot more algorithms. For example, you can optimize a evaluator using following code:

```python
from mpopt.algorithms.LoTFWA import LoTFWA
alg = LoTFWA()
opt_val = alg.optimize(evaluator)
```

You can also get and adjust the default params of the algorithm:

```python
params = alg.default_params()
alg.set_params(params)
```

## Contributing

Please follow the README.md in each module for requirements to contirbutes.

If you have any question, contact Yifeng Li (liyifeng0039@gmail.com) or Yifan Liu(liuyifan731@163.com).

## License
This source code is licensed under GPL v3. License is avaliable [here](https://github.com/CavalloneChen/mpopt/blob/master/LICENSE).

## Definitions

- **EA**: Evolutionary Algorithm.

- **SIOA**: Swarm Intelligence Optimization Algorithm.



