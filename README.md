# python-convolution

This code was made as part of a Scientific Project executed in [Unimontes](https://unimontes.br/) and financed by [FAPEMIG](http://www.fapemig.br/).  

## Dependencies

Make sure to install [NumPy](https://numpy.org/install/) and [Matplotlib](https://matplotlib.org/stable/users/installing/index.html).  

Execute the following commands in your terminal:  
- `python -m pip install -U pip`
- `python -m pip install -U matplotlib`
- `python -m pip install -U numpy`

## Introduction

This code uses Python libraries to execute convolution in functions or images, as well mas applying the convolution theorem to solve mathematical problems, like the differential [Possion's Problem](https://en.wikipedia.org/wiki/Poisson%27s_equation). The [Convolution Theorem](https://en.wikipedia.org/wiki/Convolution_theorem) especifies that, given a certain function C, that is the convolution result of the functions A and B, if B and C is known, it is possible to recover A using the Inverse Fourier Transform.  

The two methods exposed in this project:  
- **Linear**, which uses the kernel mask values to build a solvable equation system;  
- **Fourier**, which executes the [2D Inverse Fourier Transform](https://en.wikipedia.org/wiki/Fourier_inversion_theorem) in functions C and B to recover function A;  

