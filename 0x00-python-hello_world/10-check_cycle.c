#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: singly linked list
 *
 * Return: 0 OR 1
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	hare = list, tortoise = list;

	while (tortoise != NULL && hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (hare == tortoise)
		{
			return (1);
		}
	}

	return (0);
}
