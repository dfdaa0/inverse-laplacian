# poisson-problem

This code was made as part of a Scientific Project executed in [Unimontes](https://unimontes.br/) and financed by [FAPEMIG](http://www.fapemig.br/).  

## Dependencies

Make sure to install [NumPy](https://numpy.org/install/) and [Matplotlib](https://matplotlib.org/stable/users/installing/index.html).  

Execute the following commands in your terminal:  
- `python -m pip install -U pip`
- `python -m pip install -U matplotlib`
- `python -m pip install -U numpy`

## Introduction

This code implements the math behind the recovering of images or functions from the laplacian form of those, applying the convolution theorem, assuming that the Laplacian of an image can be simulated through a 3x3 mask called "Kernel".  
The [Convolution Theorem](https://en.wikipedia.org/wiki/Convolution_theorem) especifies that, given a certain function C, that is the convolution result of the functions A and B, if B and C is known, it is possible to recover A using the Inverse Fourier Transform.  

## Steps:

1. Calculate the Fourier Transform of C and store it in X;
2. Calculate the Fourier Transform of B and store it in Y;
3. Divide X by Y and store it in Z;
4. Calculate the Inverse Fourier Transform of Z;

Note that the Fourier operator results in complex numbers, which obligates the use of `numpy.real()` function.  
