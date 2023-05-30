#ulizacao da classe list
vetor=[10,11,12]
print(vetor)
print(vetor[2])

#utilizando array, obs: capacidade de conter apenas elementos homogeneos
from array import array
vetor2=array('i', [10,11,12]) #int
print(vetor2)
print(vetor2[2])

#com numpy
import numpy as np
vetor3 = np.array([10,11,12])
print(vetor3)
print(vetor3[2])