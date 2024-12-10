import numpy as np
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

class NumPYPandasBasics:
	def __init__(self):
		print("Привет")

	def numpy_example(self):
		print("\n за неделю темп")
		temp = np.array([20, 22, 19, 21, 23, 24])
		print("Темп: ", temp )