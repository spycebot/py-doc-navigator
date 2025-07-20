# py-doc-navigator
Navigate Python module documentation in the terminal

## Summary

Python provides a robust system for internal documentation. Modules, classes and methods contain text in tripple quotes just underneath their declaration which is intended to contain summary and details about the module itself, the so-called "doc". The doc is accessed by module.__doc__. When looking at the NumPy module, we noticed a large number of methods, and these methods were by-in-large internally documented. So we developed code to explore these docs.

Having completed that, we thought it would be useful to generalise the script for use with any module available in the local environment.

### Problem

THere are times when we have access to a Python environment at the same time that we do not have access to the internet. Therefore, it is important to be able to understand the Python modules that are already installed on our system / in the current environment, without recourse to documentation that is to be found on the internet.

### Data

The data for this exercise is derived from the Python environment itself. For testing purposes we used NumPy and its internal documentation.

### Model

f(x) = eval(module.__doc__)

### Method

In order to draw out the internal documentation with Python code, we make heavy use of the eval() function.


### Conclusion

It is important to be able to make use of a Python terminal or virtual environment even in the case where we do not have access to online documentation. Many systems have Python docs downloaded, but some do not.