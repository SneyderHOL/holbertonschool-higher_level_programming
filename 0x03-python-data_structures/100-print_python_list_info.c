#include <Python.h>
/**
 * print_python_list_info - function that print some basic info about Python
 * lists.
 * @p: PyObject element
 *
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	PyObject *item = NULL;

	if (p == NULL || !PyList_Check(p))
		return;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zu\n", size);
	printf("[*] Allocated = %zu\n", ((PyListObject *) p)->allocated);

	for (; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zu: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
