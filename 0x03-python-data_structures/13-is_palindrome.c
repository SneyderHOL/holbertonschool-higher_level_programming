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
	listint_t *aux = NULL, *middle = NULL;
	int count = 0;

	if (head == NULL || *head == NULL)
		return (1);
	aux = *head, middle = *head;
	for (count = 1; aux->next != NULL; count++)
	{
		middle = middle->next;
		aux = aux->next;
		if (aux->next != NULL)
			aux = aux->next, count++;
	}
	printf("%d\n", count);
	if (*head == aux)
		return (1);
	aux = *head;
	middle = reverse_listint(&middle);
	while (middle->next != NULL)
	{
		if (aux->n == middle->n)
		{
			aux = aux->next;
			middle = middle->next;
		}
		else
			return (0);
	}
	return (1);
}
/**
 * reverse_listint - function that reverse a listint_t linked list.
 * @head: pointer to the head of a listint element
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *aux = *head;
	listint_t *tmp = *head;

	if (*head == NULL)
		return (NULL);
	while (aux->next != NULL)
	{
		if (tmp != *head)
			tmp = *head;
		*head = aux->next;
		aux->next = (*head)->next;
		(*head)->next = tmp;
	}
	return (*head);
}
