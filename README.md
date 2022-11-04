# inverse-laplacian

This code was made as part of a Scientific Project executed in [Unimontes](https://unimontes.br/) and financed by [FAPEMIG](http://www.fapemig.br/).  

## Dependencies

- [NumPy](https://numpy.org/install/)
- [Matplotlib](https://matplotlib.org/stable/users/installing/index.html)
- [OpenCV](https://opencv.org/).  

Execute the following commands in your terminal:  
- `python -m pip install -U pip`
- `python -m pip install -U matplotlib`
- `python -m pip install -U numpy`
- `python -m pip install opencv-contrib-python-headless`

## Introduction

This code implements the math behind the recovering of images or functions from the laplacian form of those, applying the convolution theorem, assuming that the Laplacian of an image can be simulated through a 3x3 mask called "Kernel", that filters the image, highlighting its borders.  
It is also possible to filter a image using a personalized kernel of your choice, changing the values of it and seeing the results. Try using a gaussian or an average one and see the blurry result.    
The [Convolution Theorem](https://en.wikipedia.org/wiki/Convolution_theorem) especifies that, given a certain function C, that is the convolution result of the functions A and B, if B and C is known, it is possible to recover A using the Inverse Fourier Transform.  

## Steps taken by the code

1. Imports a image/function via a given path;
2. Filters the image using the specified kernel;
3. Calculates the Fourier Transform of the filtered image;
4. Divides it by the Fourier Transform of the kernel (sometimes it is necessary to switch 0 values to 1 because of division domain problems);
5. Calculates the Inverse Fourier Transform of the result, which gives the original image;

Note that the Fourier operator results in complex numbers, which obligates the use of `numpy.real()` function.  
