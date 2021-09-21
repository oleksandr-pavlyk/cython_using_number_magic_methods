class Quaternion:
    x_ = 0.
    y_ = 0.
    z_ = 0.
    w_ = 0.0

    def __init__(self, x=0., y=0., z=0., w=0.):
        self.x_ = x
        self.y_ = y
        self.z_ = z
        self.w_ = w

    @property
    def x(self):
        return self.x_

    @x.setter
    def x(self, v):
        self.x_ = v

    @property
    def y(self):
        return self.y_

    @y.setter
    def y(self, v):
        self.y_ = v

    @property
    def z(self):
        return self.z_

    @z.setter
    def z(self, v):
        self.z_ = v

    @property
    def w(self):
        return self.w_

    @w.setter
    def w(self, v):
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
    x1_q = isinstance(x1, Quaternion)
    x2_q = isinstance(x2, Quaternion)

    if (x1_q and x2_q):
        return _multiply_Quaternion(x1, x2)
    elif x1_q:
        return _multiply_scalar(x1, x2)
    elif x2_q:
        return _multiply_scalar(x2, x1)
    else:
        return x1 * x2

def add(x1, x2):
    x1_q = isinstance(x1, Quaternion)
    x2_q = isinstance(x2, Quaternion)

    if (x1_q and x2_q):
        return _add_Quaternion(x1, x2)
    elif x1_q:
        return _add_scalar(x1, x2)
    elif x2_q:
        return _add_scalar(x2, x1)
    else:
        return x1 + x2



def _multiply_Quaternion(q1, q2):
    return Quaternion(
        q1.x_ * q2.x_ - q1.y_ * q2.y_ - q1.z_ * q2.z_ - q1.w_ * q2.w_,  # x
        q1.x_ * q2.y_ + q1.y_ * q2.x_ + q1.z_ * q2.w_ - q1.w_ * q2.z_,  # y
        q1.x_ * q2.z_ + q1.z_ * q2.x_ - q1.y_ * q2.w_ + q1.w_ * q2.y_,  # z
        q1.x_ * q2.w_ + q1.w_ * q2.x_ + q1.y_ * q2.z_ - q1.z_ * q2.y_   # w
    )


def _multiply_scalar(q, f):
    return Quaternion(
        f * q.x_, f * q.y_, f * q.z_, f * q.w_
    )


def _add_scalar(q, a):
    return Quaternion(
        a + q.x_, q.y_, q.z_, q.w_
    )


def _add_Quaternion(q1, q2):
    return Quaternion(
        q1.x_ + q2.x_,
        q1.y_ + q2.y_,
        q1.z_ + q2.z_,
        q1.w_ + q2.w_
    )
