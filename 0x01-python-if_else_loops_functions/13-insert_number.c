#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: linked list head node
 * @number: value to be added to a sorted linked list
 *
 * Return: New node's address OR NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *insert;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);

	if (*head == NULL || (*head)->n >= number)
	{
		insert->n = number;
		insert->next = *head;
		*head = insert;
	}
	else
	{
		current = *head;
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		insert->n = number;
		insert->next = current->next;
		current->next = insert;
	}

	return (insert);
}

