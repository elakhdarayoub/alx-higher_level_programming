#include "lists.h"

/**
 * insert_node - Insert node at a list
 * head: The first element in list
 * number: The data to insert
 * 
 * Return: Pointer to list
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *inserted = malloc(sizeof(listint_t));
    if (!head || !inserted)
        return NULL;

    inserted->n = number;
    inserted->next = *head;
    *head = inserted;

    return *head;
}