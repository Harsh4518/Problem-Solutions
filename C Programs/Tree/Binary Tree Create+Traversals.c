#include<stdio.h>
#include<malloc.h>

struct node
{
	int data;
	struct node *left;
	struct node *right;
};

struct node *newnode;

struct node *create()
{
	newnode=(struct node*)malloc(sizeof(struct node));
	
	int element;
	
	printf("Enter the Element:\n");
	scanf("%d",&element);
	
	if(element==-1)
	return 0;
	
	else
	{
	printf("Enter the left Child:\n");
	create(newnode->left);
	
	printf("Enter the right Child:\n");
	create(newnode->right);
    }
	return newnode;
}

struct node* inorder(struct node *root)
{
	if(root==0) 
	return 0;
	
	inorder(root->left);
	printf("%d,",root->data);
	inorder(root->right);
}

struct node* preorder(struct node *root)
{
	if(root==0) 
	return 0;
	
	printf("%d,",root->data);
	inorder(root->left);	
	inorder(root->right);
}

struct node* postorder(struct node *root)
{
	if(root==0) 
	return 0;
	
	inorder(root->left);	
	inorder(root->right);
	printf("%d,",root->data);
}

void main()
{
	struct node*root;
	root=create();
	
	printf("Inorder Traversal:\n");
	inorder(root);
	
	printf("Preorder Traversal:\n");
	preorder(root);
	
	printf("Postorder Traversal:\n");
	postorder(root);
	
}



