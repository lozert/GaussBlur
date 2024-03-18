# Import required libraries
# import torch
# import torchvision
# from torchvision.io import read_image
# import torchvision.transforms as T
import numpy as np 

gayss_matrix = np.array([[0.00000067, 0.00002292, 0.00019117, 0.00038771, 0.00019117, 0.00002292, 0.00000067],
                        [0.00002292, 0.00078633, 0.00655965, 0.01330373, 0.00655965, 0.00078633, 0.00002292],
                        [0.00019117, 0.00655965, 0.05472157, 0.11098164, 0.05472157, 0.00655965, 0.00019117],
                        [0.00038771, 0.01330373, 0.11098164, 0.22508352, 0.11098164, 0.01330373, 0.00038771],
                        [0.00019117, 0.00655965, 0.00655965, 0.11098164, 0.05472157, 0.00655965, 0.00019117],
                        [0.00002292, 0.00078633, 0.00655965, 0.01330373, 0.00655965, 0.00078633, 0.00002292],
                        [0.00000067, 0.00002292, 0.00019117, 0.00038771, 0.00019117, 0.00002292, 0.00000067]])

low_gayss_matrix = np.array([[0.4, 0.3, 0.2],
                             [0.4, 0.3, 0.2],
                             [0.4, 0.3, 0.2]])


img = [[1, 2, 3, 1, 1, 1, 1],
       [2, 3, 1, 1, 1, 1, 1],
       [1, 4, 5, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1]]



new = np.zeros((len(img) + len(low_gayss_matrix) - 1, len(img[0]) + len(low_gayss_matrix[0]) - 1) )
new[1: -int(len(low_gayss_matrix)/2), 1: -int(len(low_gayss_matrix[0])/2)] = img #Расширенная матрица на нули, чтоб матрицу можно было прогнать по всем элементам не сварачивая основное

y = np.zeros((len(img), len(img[0])))

def sumMatrix(small_matrix): # Свёртка 
    summ = 0

    for i in range(len(small_matrix)):
        for j in range(len(small_matrix[0])):
            # print(f"SM {small_matrix[i][j]} * LGM {low_gayss_matrix[i][j]} \n")
            summ += small_matrix[i][j] * low_gayss_matrix[i][j]
    
    return summ

for i in range(1, len(new) - 1):
    for j in range(1, len(new) - 1):
        
        small_matrix = np.zeros((3,3))
        
        small_matrix = new[i-1:i+2,j-1:j+2]
        # print(small_matrix)
        
        y[i-1][j-1] = sumMatrix(small_matrix)
        
      
print(y)


step_left = len(img[0]) - len(gayss_matrix[0])
step_down = len(img) - len(gayss_matrix)

print(gayss_matrix.shape)


# read the jpg image
# pic = read_image('nature.jpg')
# print(pic.shape)
# # convert this torch tensor to PIL image 
# PIL_img = T.ToPILImage()(pic)

# # display result
# PIL_img.show()
