import numpy as np

class NLDESolver:
  def __init__(self, func):
    self._func = func
  
  def solve(self, y1_range, y2_range, axis="x"):
    return self._solve(y1_range, y2_range, axis)
  
  def _solve(self, y1_range, y2_range, axis):
    Y1, Y2 = np.meshgrid(y1_range, y2_range)
    u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)
    NI, NJ = Y1.shape
    js = []
    for i in range(NI):
      min_j = 0
      min_v = 100
      for j in range(NJ):
        x = Y1[i, j]
        y = Y2[i, j]
        yprime = self._func([x, y])
        v[i,j] = yprime

        if min_v >= abs(v[i,j]):
          min_v = abs(v[i,j])
          min_j = j

      js.append(min_j)
    
    if axis == "x":
      return [y1_range[j] for j in js]
    return [y2_range[j] for j in js]