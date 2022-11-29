#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 *
 * @head: Received during function call
 * @number: Received during function call
 *
 * Return: Always listint_t pointer
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert;
	listint_t *current;

	current = *head;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);

	if (*head == NULL)
		*head = insert;
	else
	{
		if (current->n < number)
			current = current->next;
		current->next = insert;
	}

	return (insert);
}
