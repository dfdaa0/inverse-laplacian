# python-convolution

This code was made as part of a Scientific Project executed in [Unimontes](https://unimontes.br/) and financed by [FAPEMIG](http://www.fapemig.br/).  

## Introduction

It uses Python libraries to execute convolution in functions or images. The [Convolution Theorem](https://en.wikipedia.org/wiki/Convolution_theorem) especifies that, given a certain function A that has suffered the convolution process with a function B that made the function C, if the B function is known, it is possible to make the inverse process, called Deconvolution, and recover the original function A.  

The two methods exposed in this project:  
- **Linear**, which uses the kernel mask values to build a solvable equation system;  
- **Fourier**, which executes the [2D Inverse Fourier Transform](https://en.wikipedia.org/wiki/Fourier_inversion_theorem) in functions C and B to recover function A;  

## Dependencies

Make sure to install [NumPy](https://numpy.org/install/) and [Matplotlib](https://matplotlib.org/stable/users/installing/index.html)  
