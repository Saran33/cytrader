cdef extern from "Python.h":
    const char* PyUnicode_AsUTF8(object unicode)

from libc.stdlib cimport malloc, free
from libc.string cimport strcpy, strlen


cdef char ** _cstring_array(str[:] list_str):
    cdef char **ret = <char **>malloc(len(list_str) * sizeof(char *))
    for i in xrange(len(list_str)):
        ret[i] = PyUnicode_AsUTF8(list_str[i])
    return ret

cpdef cstring_array_write(list list_str, object out):
    cdef char **c_arr = _cstring_array(list_str)
    for l in xrange(len(list_str)):
        out.write(c_arr[l] + '\n')
    free(c_arr)


cpdef cstring_write(char* string, object out):
    cdef char *c_str = <char *>malloc((strlen(string)+1) * sizeof(char))
    strcpy(c_str, string)
    py_string = c_str
    out.write(py_string + '\n')
    free(c_str)
