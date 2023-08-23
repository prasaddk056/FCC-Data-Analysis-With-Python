import numpy as np

def calculate(list):
  if(len(list) != 9):
    raise ValueError('List must contain nine numbers.')
  else:

    matrix = np.array(list).reshape(3,3)

    mean = [(matrix.mean(axis = 0)).tolist() ,(matrix.mean(axis = 1)).tolist(), matrix.flatten().mean()]

    var = [(matrix.var(axis = 0)).tolist() ,(matrix.var(axis = 1)).tolist(), matrix.flatten().var()]

    std = [(matrix.std(axis = 0)).tolist() ,(matrix.std(axis = 1)).tolist(), matrix.flatten().std()]

    maxi = [(matrix.max(axis = 0)).tolist() ,(matrix.max(axis = 1)).tolist(), matrix.flatten().max()]

    mini = [(matrix.min(axis = 0)).tolist() ,(matrix.min(axis = 1)).tolist(), matrix.min().min()]

    add = [(matrix.sum(axis = 0)).tolist() ,(matrix.sum(axis = 1)).tolist(), matrix.flatten().sum()]

  calculations = {
    'mean':                mean,
    'variance':            var,
    'standard deviation':  std,
    'max':                 maxi,
    'min':                 mini,
    'sum':                 add
  }
  return calculations