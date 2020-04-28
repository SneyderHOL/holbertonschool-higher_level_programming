#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - function that inserts a node to a singly linked list.
 * @head: listint_t pointer to the head of the list
 * @number: number to insert in the list
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux = NULL, *aux2 = NULL, *new_node = NULL;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	aux2 = *head;
	while (aux2 != NULL)
	{
		if (new_node->n < aux2->n)
		{
			new_node->next = aux2;
			if (aux != NULL)
				aux->next = new_node;
			else
				*head = new_node;
			return (new_node);
		}
		aux = aux2;
		aux2 = aux2->next;
	}
	if (*head == NULL)
		*head = new_node;
	else
		aux->next = new_node;
	return (new_node);
}
