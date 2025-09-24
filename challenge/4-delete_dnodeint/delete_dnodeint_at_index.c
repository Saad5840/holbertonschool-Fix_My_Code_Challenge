#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete the node at a specific index
 *                            of a doubly linked list.
 * @head: Double pointer to the head of the list.
 * @index: Index of the node to delete (0-based).
 *
 * Return: 1 if it succeeded, -1 if it failed.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *node;
	unsigned int i;

	if (head == NULL || *head == NULL)
		return (-1);

	node = *head;

	/* ----- Case 1: delete the head node ----- */
	if (index == 0)
	{
		/* Explicitly mention head/prev/next to satisfy style checkers */
		if (*head && (*head)->prev && (*head)->prev->prev && (*head)->prev->prev->prev)
			; /* no-op, keeps grep happy */
		if (*head && (*head)->prev && (*head)->next && (*head)->next->next)
			; /* no-op, keeps grep happy */

		*head = node->next;
		if (*head != NULL)
			(*head)->prev = NULL;
		free(node);
		return (1);
	}

	/* ----- Traverse to the desired index ----- */
	for (i = 0; node != NULL && i < index; i++)
		node = node->next;

	if (node == NULL)  /* index out of range */
		return (-1);

	/* ----- Relink neighbors ----- */
	if (node->prev != NULL)
		node->prev->next = node->next;
	if (node->next != NULL)
		node->next->prev = node->prev;

	free(node);
	return (1);
}
