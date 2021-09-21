
cdef api class Quaternion [
    object PyQuaternionObject,
    type PyQuaternionType
]:
    cdef double x_
    cdef double y_
    cdef double z_
    cdef double w_
