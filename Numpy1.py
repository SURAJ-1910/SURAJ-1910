#Q1
#1. Create a null vector of size 10 but the fifth value which is 1.

import numpy as np
array_list=np.zeros(10)
array_list[4]=1
print("Null vector of size 10 with the fifth value which is 1 : " , array_list)


#Q2
#Create a vector with values ranging from 10 to 49.
import numpy as np
vector_range = np.arange(10,50)
print("vector range:")
print(vector_range)


#Q3
# Create a 3x3 matrix with values ranging from 0 to 8
import numpy as np
values=np.arange(0,9).reshape((3,3))
print("3x3 matrix with values ranging from 0 to 8 : " ,values)


#Q4
#Find indices of non-zero elements from [1,2,0,0,4,0]

import numpy as np
arr_1 = np.array([1,2,0,0,4,0])
  
print ("Input  array : ", arr_1)
    
arr_2 = np.nonzero(arr_1)
print ("Indices of non zero elements : ", arr_2) 


#Q5
#Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np
random_array = np.random.random((10,10))
print("Original Array:")
print(random_array) 
print()
print()
array_min_value = random_array.min()
array_max_value = random_array.max()

print("Minimum Value:",array_min_value)
print("Maximum Value:",array_max_value)


#Q6
# Create a random vector of size 30 and find the mean value.
import numpy as np
size = np.random.random(30)
mean_value = size.mean()
print ("The mean value of random vector of size 30: ", mean_value)