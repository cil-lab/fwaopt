# Compile the Benchmark Functions


Considering the running efficiency, all test functions are written in C language. Therefore, the test function needs to be compiled before running.

### For Linux

For Linux users, please run the following command to compile and install

```bash
make clean && make
```
### For Windows

For Windows users, please make sure you have a suitable compiler in your system. we recommend to use MinGW. You can also use Microsoft Visual C++ 14.0 or higher. You can find MinGW on [https://github.com/skeeto/w64devkit/releases](https://github.com/skeeto/w64devkit/releases).

First run the following command to compile after the compiler has been installed in your system.

```text
gcc -c icsi2022.c icsi2022.h
ar rcs libicsi2022.a icsi2022.o
```

Then run the following command to finish the compilation.

```text
python setup.py build_ext --inplace
```

Note the folder location where you run the above command.