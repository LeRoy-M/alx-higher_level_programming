#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: Head of the list
 *
 * Return: Always 0 OR 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *fwd, *bwd;

	fwd = malloc(sizeof(listint_t));
	bwd = malloc(sizeof(listint_t));
	if (fwd == NULL || bwd == NULL)
		return (0);

	fwd = *head;
	bwd = *head;

	if (*head == NULL)
		return (1);
	while (bwd->next != NULL)
	{
		bwd = bwd->next;
	}
	if (fwd->n == bwd->n)
		return (1);

	return (0);
}
