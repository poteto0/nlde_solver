# Nonlinear Differential Equation Solver
Solve Nonlinear Differential Equations approximately.

```sh
pip install git+https://github.com/poteto0/nlde_solver.git
```

```python
import nlde_solver as nldes

solver = nldes.NLDESolver(func=function)
```

The function must take a two-dimentional argument and return a one-dimensional return value. The arguments should be array.

```math
\frac{dx}{dt} = \alpha x - (1-\alpha)
```

```python
def ex(x=[x,y]):
  return alpha*x - (1-alpha)*y
```

This pkg can solve nonlinear-differential-equations approximately.
An approximate solution with the smallest gradient within a given search range is searched. If there is sufficient search range, this will be a nullcline.

```python
y1 = np.linspace(..., ..., ...)
y2 = np.linspace(..., ..., ...)
ans = solver.solve(y1, y2)
```