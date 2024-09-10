## Requirements for optimizer implementation:

1. File and the optimizer class should have the same name.

2. Provide self.default_params(benchmark=benchmark) which return algorihtm params dictionary for given benchmark information.

3. Provide self.set_params(params) which accept a parameters dictionary to set algorithm params.