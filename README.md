# Build

```bash
python setup.py build_ext --inplace
```

# Problem

```python
import quarternion as m

q = m.Quaternion(1, 2, 3, 4)

print(q * 2.0)  # works as expected, calls `Quaternion.__mul__(q, 2.0)`
                # magic method

print(2.0 * q)  # raises TypeError.
                # Python calls `Quaternion.__mul__(2.0, q)`,
		# rather than `Quaternion.__rmul__(q, 2.0)` as expected

q.__rmul__(2.0) # also raises, and prints message from `__mul__`
                # does not print any messages from `__rmul__`

```

This is in contrast to behavior of Python extension

```python
import py_quarternion as m

q = m.Quaternion(1, 2, 3, 4)

print(q * 2.0)  # works as expected, calls `Quaternion.__mul__(q, 2.0)`
                # magic method

print(2.0 * q)  # work as expected, calls `Quaternion.__rmul__(q, 2.0)`

q.__rmul__(2.0) # print message from `__rmul__` and give expected result

```

This is the sample output

```
Python 3.7.10 (default, Jun  4 2021, 06:52:02)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.27.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import py_quaternion as m

In [2]: q = m.Quaternion(1., 2., 3., 4.)

In [3]: q * 2.0
__mul__ <class 'py_quaternion.Quaternion'> <class 'float'>
Out[3]: Quaternion(2.0, 4.0, 6.0, 8.0)

In [4]: 2.0 * q
__rmul__ <class 'py_quaternion.Quaternion'> <class 'float'>
Out[4]: Quaternion(2.0, 4.0, 6.0, 8.0)

In [5]: q.__rmul__(2.0)
__rmul__ <class 'py_quaternion.Quaternion'> <class 'float'>
Out[5]: Quaternion(2.0, 4.0, 6.0, 8.0)

In [6]: import quaternion as cy_m

In [7]: qq = cy_m.Quaternion(1., 2., 3., 4.)

In [8]: qq * 2.0
('__mul__', <class 'quaternion.Quaternion'>, <class 'float'>)
Out[8]: Quaternion(2.0, 4.0, 6.0, 8.0)

In [9]: 2.0 * qq
('__mul__', <class 'float'>, <class 'quaternion.Quaternion'>)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-32f6ebc95910> in <module>
----> 1 2.0 * qq

/localdisk/work/quaternion.pyx in quaternion.Quaternion.__mul__()
     84             return _multiply_scalar(self, other)
     85         elif isinstance(other, Quaternion):
---> 86             return _multiply_Quaternion(self, other)
     87         return NotImplemented
     88

TypeError: Cannot convert float to quaternion.Quaternion
```
