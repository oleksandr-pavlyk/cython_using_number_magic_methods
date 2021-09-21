

"""
       1    i    j    k
     +------------------
   1 | 1    i    j    k
   i | i   -1    k   -j
   j | j   -k   -1    i
   k | k    j   -i    -1
"""
cdef Quaternion _multiply_Quaternion(Quaternion q1, Quaternion q2):
    return Quaternion.__new__(
        Quaternion,
        q1.x_ * q2.x_ - q1.y_ * q2.y_ - q1.z_ * q2.z_ - q1.w_ * q2.w_,  # x
        q1.x_ * q2.y_ + q1.y_ * q2.x_ + q1.z_ * q2.w_ - q1.w_ * q2.z_,  # y
        q1.x_ * q2.z_ + q1.z_ * q2.x_ - q1.y_ * q2.w_ + q1.w_ * q2.y_,  # z
        q1.x_ * q2.w_ + q1.w_ * q2.x_ + q1.y_ * q2.z_ - q1.z_ * q2.y_   # w
    )


cdef Quaternion _multiply_scalar(Quaternion q, double f):
    return Quaternion.__new__(
        Quaternion, f * q.x_, f * q.y_, f * q.z_, f * q.w_
    )


cdef Quaternion _add_scalar(Quaternion q, double a):
    return Quaternion.__new__(
        Quaternion, a + q.x_, q.y_, q.z_, q.w_
    )

cdef Quaternion _add_Quaternion(Quaternion q1, Quaternion q2):
    return Quaternion.__new__(
        Quaternion,
        q1.x_ + q2.x_,
        q1.y_ + q2.y_,
        q1.z_ + q2.z_,
        q1.w_ + q2.w_
    )


cdef class Quaternion:
    def __cinit__(self, double x=0., double y=0., double z=0., double w=0.):
        self.x_ = x
        self.y_ = y
        self.z_ = z
        self.w_ = w

    property x:
        def __get__(self):
            return self.x_
        def __set__(self, double v):
            self.x_ = v

    property y:
        def __get__(self):
            return self.y_
        def __set__(self, double v):
            self.y_ = v

    property z:
        def __get__(self):
            return self.z_
        def __set__(self, double v):
            self.z_ = v

    property w:
        def __get__(self):
            return self.w_
        def __set__(self, double v):
            self.w_ = v

    def __repr__(self):
        return ("Quaternion(" +
                str(self.x_) + ", " +
                str(self.y_) + ", " +
                str(self.z_) + ", " +
                str(self.w_) + ")"
        )

    def __mul__(self, other):
        print("__mul__", type(self), type(other))
        if isinstance(other, float):
            return _multiply_scalar(self, other)
        elif isinstance(other, Quaternion):
            return _multiply_Quaternion(self, other)
        return NotImplemented

    def __add__(self, other):
        print("__add__", type(self), type(other))
        if isinstance(other, float):
            return _add_scalar(self, other)
        elif isinstance(other, Quaternion):
            return _add_Quaternion(self, other)
        return NotImplemented

    def __rmul__(self, other):
        print("__rmul__", type(self), type(other))
        if isinstance(other, float):
            return _multiply_scalar(self, other)
        elif isinstance(other, Quaternion):
            return _multiply_Quaternion(other, self)
        return NotImplemented


def multiply(x1, x2):
    cdef bint x1_q = isinstance(x1, Quaternion)
    cdef bint x2_q = isinstance(x2, Quaternion)

    if (x1_q and x2_q):
        return _multiply_Quaternion(x1, x2)
    elif x1_q:
        return _multiply_scalar(x1, x2)
    elif x2_q:
        return _multiply_scalar(x2, x1)
    else:
        return x1 * x2

def add(x1, x2):
    cdef bint x1_q = isinstance(x1, Quaternion)
    cdef bint x2_q = isinstance(x2, Quaternion)

    if (x1_q and x2_q):
        return _add_Quaternion(x1, x2)
    elif x1_q:
        return _add_scalar(x1, x2)
    elif x2_q:
        return _add_scalar(x2, x1)
    else:
        return x1 + x2
