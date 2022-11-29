#include "lists.h"

/**
 * is_palindrome - Checks if singly linked list is a palindrome
 *
 * @head: Received input during function call
 *
 * Return: '0' if not a palindrome, '1' if is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint front, back;

	if (*head == NULL)
		return (1);

	front = *head;
	back = *head;
	while (front->next != NULL)
	{
		return (0);
	}
}
