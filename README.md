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