#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - function that checks if a singly linked list is a
 * palindrome
 * @head: pointer to the head of the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL, *tmp = NULL;
	int count = 0, aux = 0;

	if (head == NULL || *head == NULL)
		return (1);
	start = *head, end = *head;
	for (count = 1; end->next != NULL; count++)
		end = end->next;
	if (*head == end)
		return (1);
	for (aux = 1; aux <= count / 2; aux++)
	{
		if (count % 2 == 0 && aux == count / 2)
		{
			if (start->n == end->n)
				return (1);
			else
				return (0);
		}
		if (start->n == end->n)
		{
			start = start->next;
			tmp = start;
			while (tmp->next != end)
				tmp = tmp->next;
			end = tmp;
		}
		else
			return (0);
	}
	return (1);
}
