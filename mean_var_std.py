import numpy as np

def calculate(values):
    if len(values) < 9: raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(values).reshape((3,3))
    #Mean Axis 1
    transposed_matrix = matrix.transpose()
    mean_axis1_0 = np.sum(transposed_matrix[0])/3
    mean_axis1_1 = np.sum(transposed_matrix[1])/3
    mean_axis1_2 = np.sum(transposed_matrix[2])/3
    mean_axis1 = [mean_axis1_0, mean_axis1_1, mean_axis1_2]
    
    #Mean Axis 2
    mean_axis2_0 = np.sum(matrix[0])/3
    mean_axis2_1 = np.sum(matrix[1])/3
    mean_axis2_2 = np.sum(matrix[2])/3
    mean_axis2 = [mean_axis2_0, mean_axis2_1, mean_axis2_2]
    
    #Mean Flat 
    mean_flat = np.sum(values) / 9
            

    #Variance Axis 1
    var_axis1_0 = np.var(transposed_matrix[0])
    var_axis1_1 = np.var(transposed_matrix[1])
    var_axis1_2 = np.var(transposed_matrix[2])
    var_axis1 = [var_axis1_0,var_axis1_1,var_axis1_2]

    #Variance Axis 2
    var_axis2_0 = np.var(matrix[0])
    var_axis2_1 = np.var(matrix[1])
    var_axis2_2 = np.var(matrix[2])
    var_axis2 = [var_axis2_0,var_axis2_1,var_axis2_2]

    #Variance Flat
    var_flat = np.var(values)

    #Standard Deviation Axis 1
    std_axis1_0 = np.std(transposed_matrix[0])
    std_axis1_1 = np.std(transposed_matrix[1])
    std_axis1_2 = np.std(transposed_matrix[2])
    std_axis1 = [std_axis1_0,std_axis1_1,std_axis1_2]

    #Standard Deviation Axis 2
    std_axis2_0 = np.std(matrix[0])
    std_axis2_1 = np.std(matrix[1])
    std_axis2_2 = np.std(matrix[2])
    std_axis2 = [std_axis2_0,std_axis2_1,std_axis2_2]

    #Standard Deviation Flat
    std_flat = np.std(values)

    #Max Axis 1
    max_axis1_0 = np.max(transposed_matrix[0])
    max_axis1_1 = np.max(transposed_matrix[1])
    max_axis1_2 = np.max(transposed_matrix[2])
    max_axis1 = [max_axis1_0,max_axis1_1,max_axis1_2]

    #Max Axis 2
    max_axis2_0 = np.max(matrix[0])
    max_axis2_1 = np.max(matrix[1])
    max_axis2_2 = np.max(matrix[2])
    max_axis2 = [max_axis2_0,max_axis2_1,max_axis2_2]

    #Max Flat
    max_flat = np.max(values)

    #Min Axis 1
    min_axis1_0 = np.min(transposed_matrix[0])
    min_axis1_1 = np.min(transposed_matrix[1])
    min_axis1_2 = np.min(transposed_matrix[2])
    min_axis1 = [min_axis1_0,min_axis1_1,min_axis1_2]

    #Min Axis 2
    min_axis2_0 = np.min(matrix[0])
    min_axis2_1 = np.min(matrix[1])
    min_axis2_2 = np.min(matrix[2])
    min_axis2 = [min_axis2_0,min_axis2_1,min_axis2_2]

    #Min Flat
    min_flat = np.min(values)

    #Sum Axis 1
    sum_axis1_0 = np.sum(transposed_matrix[0])
    sum_axis1_1 = np.sum(transposed_matrix[1])
    sum_axis1_2 = np.sum(transposed_matrix[2])
    sum_axis1 = [sum_axis1_0,sum_axis1_1,sum_axis1_2]

    #Sum Axis 2
    sum_axis2_0 = np.sum(matrix[0])
    sum_axis2_1 = np.sum(matrix[1])
    sum_axis2_2 = np.sum(matrix[2])
    sum_axis2 = [sum_axis2_0,sum_axis2_1,sum_axis2_2]

    #Sum Flat
    sum_flat = np.sum(values)


    calculations  = {
        'mean': [mean_axis1, mean_axis2, mean_flat],
        'variance' : [var_axis1, var_axis2, var_flat],
        'standard deviation' : [std_axis1, std_axis2, std_flat] ,
        'min': [min_axis1, min_axis2, min_flat],
        'max': [max_axis1, max_axis2, max_flat],
        'sum': [sum_axis1, sum_axis2, sum_flat]        
    }
    return calculations
