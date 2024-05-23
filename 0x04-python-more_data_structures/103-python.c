#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
* print_python_list - prints out a python list
@p: a pointer to the pyobject
*/
void print_python_list(PyObject *p)
{
	int size, i, alloc;
	const char *type_of_ob;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		type_of_ob = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type_of_ob);
		if (strcmp(type_of_ob, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
/**
* print_python_bytes - prints the bytes of the list
* @p: a pyobject byte object
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	unsigned char i, size;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("   [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first 10 bytes: %d", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
