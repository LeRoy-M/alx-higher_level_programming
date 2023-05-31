#include <stdio.h>
/* #include <Python.h> */

/**
 * print_python_list - Prints basic info about Python lists
 *
 * @p: A PyObject
 *
 * Return: Always VOID
 */

void print_python_list(PyObject *p)
{
	if (p == NULL)
	{
		printf("[ERROR] Invalid List Object");
		fflush(stdout);
		return;
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes
 *
 * @p: A PyObject
 *
 * Return: Always VOID
 */

void print_python_bytes(PyObject *p)
{
	if (p == NULL)
	{
		printf("[ERROR] Invalid Bytes Object");
		fflush(stdout);
		return;
	}
}

/**
 * print_python_float - Prints basic info about Python floats
 *
 * @p: A PyObject
 *
 * Return: Always VOID
 */

void print_python_float(PyObject *p)
{
	if (p == NULL)
	{
		printf("[ERROR] Invalid Float Object");
		fflush(stdout);
		return;
	}
}
