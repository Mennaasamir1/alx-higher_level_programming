#include <Python.h>

void print_python_list_info(PyObject *p)
{
    long int size_of_list = PyList_Size(p);
    int i;
    PyListObject *j = (PyListObject *)p;

    printf("[*] Size of the Python List = %li\n", size_of_list);
    printf("[*] Allocated = %li\n", j->allocated);

    for(i = 0; i < size; i++)
        printf("Element %i: %s\n", i, PY_TYPE(j->ob_item[i])->tp_name);

}
