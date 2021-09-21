/* Generated by Cython 0.29.24 */

#ifndef __PYX_HAVE__quaternion
#define __PYX_HAVE__quaternion

#include "Python.h"
struct PyQuaternionObject;

/* "quaternion.pxd":2
 * 
 * cdef api class Quaternion [             # <<<<<<<<<<<<<<
 *     object PyQuaternionObject,
 *     type PyQuaternionType
 */
struct PyQuaternionObject {
  PyObject_HEAD
  double x_;
  double y_;
  double z_;
  double w_;
};

#ifndef __PYX_HAVE_API__quaternion

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#ifndef DL_IMPORT
  #define DL_IMPORT(_T) _T
#endif

#endif /* !__PYX_HAVE_API__quaternion */

/* WARNING: the interface of the module init function changed in CPython 3.5. */
/* It now returns a PyModuleDef instance instead of a PyModule instance. */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initquaternion(void);
#else
PyMODINIT_FUNC PyInit_quaternion(void);
#endif

#endif /* !__PYX_HAVE__quaternion */
