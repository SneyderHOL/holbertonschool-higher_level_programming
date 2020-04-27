#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *aux = list;

	if (list == NULL || list->next == NULL)
		return (0);
	list = list->next;
	aux = aux->next->next;
	while (list != NULL && aux != NULL && aux->next != NULL)
	{
		if (list == aux)
			return (1);
		list = list->next;
		aux = aux->next->next;
	}
	return (0);
}
