void ReverseSinglyLinkedList(struct Node*head)
{
	struct Node *current=head,*prev=0,*next=0;
	
	while(current!=0)
	{
		next=current->next;
		current->next=prev;
		prev=current;
		current=next;
	}
	
	head=prev;
}
