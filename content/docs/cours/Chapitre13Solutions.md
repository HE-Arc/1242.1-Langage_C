---
title: "Chapitre 13 : solutions"
draft: false
weight: 31
---

# Chapitre 13 : solutions
## Solutions

[1242.1.13_Listes_chainées_Correction.pdf](/pdf/1242.1.13_Listes_chainées_Correction.pdf)

### `list.h`
```c
// This module contains all declarations AND definitions
#ifndef LIST_H
#define LIST_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
	int value;
	struct node *ptr_next; // Need to use this form as typedef is not defined yet at that line
} Node;

typedef struct list
{
	Node *ptr_first;
	Node *ptr_last;
} List;

List list_init(void);
void list_display(List);
void list_inc(List);
void list_free(List*);
void list_add_node(List *, int);

List list_init(void)
{
	List list = {NULL, NULL};

	printf("Enter numbers. Enter 0 to end the list.\n");

	int status = 0;
	const int nbExpectedValues = 1;
	// Variables to store User input values
	int value;

	do
	{
		status = scanf(" %d", &value);

		// IMPORTANT: fflush(stdin) does not always work!
		// It is strongly advised NOT to use it
		// fflush(stdin);
		// Instead, empty the buffer "manually"
		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		// BIIIP to let user know when there is a problem and continue
		if (status != nbExpectedValues)
		{
			printf("\a");
		}
		else
		{
			// All good, insert new element if value is not 0
			if (value != 0)
			{
				list_add_node(&list, value);
			}
		}
	} while ((status != nbExpectedValues) || (value != 0));

	return list;
}

void list_add_node(List *list, int value)
{
	Node *elem = malloc(sizeof(Node));
	if (elem == NULL)
	{
		return;
	}

	elem->value = value;
	elem->ptr_next = NULL;

	if (list->ptr_first == NULL) // then list is empty
	{
		list->ptr_first = elem;
		list->ptr_last = elem;
	}
	else
	{
		if (elem->value > 0) // Insert in front
		{
			elem->ptr_next = list->ptr_first;
			list->ptr_first = elem;
		}
		else // Insert in back
		{
			list->ptr_last->ptr_next = elem;
			list->ptr_last = elem;
		}
	}
}

void list_display(List list)
{
	Node *p = list.ptr_first;
	while (p != NULL)
	{
		printf("%d ", p->value);
		p = p->ptr_next;
	}
	printf("\n");
}

void list_inc(List list)
{
	Node *p = list.ptr_first;
	while (p != NULL)
	{
		p->value++;
		p = p->ptr_next;
	}
}

void list_free(List *list)
{
	Node *current = list->ptr_first;
	while (current != NULL)
	{
		Node *next = current->ptr_next;
		free(current);
		current = next;
	}

	list->ptr_first = NULL;
	list->ptr_last = NULL;
}
#endif
```

### `main.c`
```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Header only library
#include "list.h"

int main(void)
{
	List list = list_init();
	list_display(list);
	list_inc(list);
	list_display(list);
	list_free(&list);
	list_display(list);

	return 0;
}
```

