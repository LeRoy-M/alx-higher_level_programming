#include <stdio.h>

/**
 * print_python_list - Prints a Python list
 *
 * @p: Python list object
 *
 * Return: void
 */

void print_python_list(PyObject *p)
{
	int size = 0;

	puts("Python list info");
	if (p == NULL)
	{
		puts("[ERROR] Invalid list Object");
		return;
	}
	else
	{
		while (p != NULL)
		{
			p++;
			size++;
		}
		puts("Size of the Python List = %i", size);
		puts("Allocated = %i", size);
		return;
	}
}

/**
 * print_python_bytes - Prints Python bytecode
 *
 * @p: Python bytecode object
 *
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	int size = 0;

	puts("Python list info");
	if (p == NULL)
	{
		puts("[ERROR] Invalid list Object");
		return;
	}
	else
	{
		while (p != NULL)
		{
			p++;
			size++;
		}
		puts("Size of the Python List = %i", size);
		puts("Allocated = %i", size);
		return;
	}
}

/**
 * print_python_float - Prints Python float
 *
 * @p: Python float object
 *
 * Return: void
 */

void print_python_float(PyObject *p)
{
	int size = 0;

	puts("Python list info");
	if (p == NULL)
	{
		puts("[ERROR] Invalid list Object");
		return;
	}
	else
	{
		while (p != NULL)
		{
			p++;
			size++;
		}
		puts("Size of the Python List = %i", size);
		puts("Allocated = %i", size);
		return;
	}
}
