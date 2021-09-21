from quaternion import Quaternion
from quaternion import multiply as q_multiply
from quaternion import add as q_add

one = Quaternion(1., 0., 0., 0.)
I = Quaternion(0., 1., 0., 0.)
J = Quaternion(0., 0., 1., 0.)
K = Quaternion(0., 0., 0., 1.)

for q1 in [one, I, J, K]:
    for q2 in [one, I, J, K]:
        comm = lambda q1, q2: q_add( q_multiply(q1, q2), q_multiply(-1.0, q_multiply(q2, q1)))
        print(comm(q1, q2), end=" ")
    print("")
