#include "pybind11/pybind11.h"
#include "quaternion.h"
#include "quaternion_api.h"

namespace py=pybind11;

class quaternion;

namespace detail {
    bool check_quaternion(PyObject *obj) {
	return PyObject_TypeCheck(obj, &PyQuaternionType) != 0;
    }

    PyObject* conv_to_quaternion(PyObject *obj) {
	if (PyFloat_Check(obj)) {
	    py::module_ m = py::module_::import("quaternion");
	    auto r = m.attr("Quaternion")(py::handle(obj));
	    return r.release().ptr();
	} else {
	    PyErr_SetString(PyExc_TypeError, "Oh no!");
	    return nullptr;
	}
    }

    PyObject* zero_quaternion() {
	py::module_ m = py::module_::import("quaternion");
	auto r = m.attr("Quaternion")();
	return r.release().ptr();
    }
}

struct Quaternion_Proxy {
    PyObject_HEAD
    double x;
    double y;
    double z;
    double w;
};

class quaternion : public py::object {
public:
    PYBIND11_OBJECT_CVT(quaternion, py::object, ::detail::check_quaternion, ::detail::conv_to_quaternion)

    quaternion() : py::object(::detail::zero_quaternion(), borrowed_t{}) {}

    double get_x() const {
	auto *proxy = reinterpret_cast<Quaternion_Proxy *>(this->ptr());
	return proxy->x;
    }
    double get_y() const {
	auto *proxy = reinterpret_cast<Quaternion_Proxy *>(this->m_ptr);
	return proxy->y;
    }
    double get_z() const {
	auto *proxy = reinterpret_cast<Quaternion_Proxy *>(this->m_ptr);
	return proxy->z;
    }
    double get_w() const {
	auto *proxy = reinterpret_cast<Quaternion_Proxy *>(this->m_ptr);
	return proxy->w;
    }
};

double norm(quaternion q) {
    auto *proxy = reinterpret_cast<Quaternion_Proxy *>(q.ptr());
    const auto sq = [](double v) -> double {return v*v;};
    double d2 = sq(proxy->x) + sq(proxy->y) + sq(proxy->z) + sq(proxy->w);

    return std::sqrt(d2);
}

PYBIND11_MODULE(a, m) {
    import_quaternion();
    m.def("norm", norm);
}
