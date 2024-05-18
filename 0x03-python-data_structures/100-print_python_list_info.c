#include <Python.h>
/**
* print_python_list_info - prints basic info about python lists
* @p: a pyobject list
*/
void print_python_list_info(PyObject *p)
{
    int size_of_list, alloc, i;
    PyObject *j;

    size_of_list = Py_SIZE(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size_of_list);
    printf("[*] Allocated = %d\n", alloc);

    for (i = 0; i < size_of_list; i++)
    {
        printf("Element %d:  ", i);
        j = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(j)->tp_name);
    }
}
