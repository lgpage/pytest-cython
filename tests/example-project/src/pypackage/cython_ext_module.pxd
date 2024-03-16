
cdef int cfoo(int a, int b) except? -1
cdef int cbar(int a, int b) except? -1 nogil
cdef inline int cspam(int a, int b) except? -1 nogil


cdef class Eggs:
    cdef:
        readonly int a
        readonly int b

    cdef int foo(Eggs self) except? -1
    cdef int bar(Eggs self) except? -1 nogil
    cdef int spam(Eggs self) except? -1 nogil
    cpdef int fubar(Eggs self)
