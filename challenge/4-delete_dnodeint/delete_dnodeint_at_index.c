#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - deletes the node at a given index
 * @head: double pointer to the head of the list
 * @index: index of the node to delete (0-based)
 *
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *node;
	unsigned int i;

	if (head == NULL || *head == NULL)
		return (-1);

	node = *head;

	/* ---- Case 1: delete the head node ---- */
	if (index == 0)
	{
		*head = node->next;
		if (*head != NULL)
			(*head)->prev = NULL;
		free(node);
		return (1);
	}

	/* ---- Walk to the node at the requested index ---- */
	for (i = 0; node != NULL && i < index; i++)
		node = node->next;

	if (node == NULL)          /* index out of range */
		return (-1);

	/* ---- Correctly unlink the node ---- */
	if (node->prev != NULL)
		node->prev->next = node->next;   /* <-- key fix */
	if (node->next != NULL)
		node->next->prev = node->prev;

	free(node);
	return (1);
}
