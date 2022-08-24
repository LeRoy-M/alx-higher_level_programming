#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 *
 * @list: Receives input during function call
 *
 * Return: '0' if no cycle, '1' if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	if (list == NULL)
		return (0);

	hare = list;
	tortoise = list;
	while (hare->next != NULL && hare->next->next != NULL)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;

		if (hare == tortoise)
			return (1);
	}

	return (0);
}
