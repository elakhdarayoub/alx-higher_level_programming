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
    listint_t *current = NULL;

    if (!head || !inserted)
        return NULL;

    current = *head;
    inserted->n = number;
 ;
    while(1)
    {
        if (current->n >= number)
        {
            inserted->next = current;
            break;
        }
        else
        {
            current = current->next;
        }
    }
    return inserted;
}