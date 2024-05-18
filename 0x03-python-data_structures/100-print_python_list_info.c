#include <Python.h>
/**
* print_python_list_info(PyObject *p) - prints information about py lists
* @p: pointer to the list
*/
void print_python_list_info(PyObject *p)
{
	int i, size, alloc;
	PyObject *j;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		j = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(j)->tp_name);
	}
}
