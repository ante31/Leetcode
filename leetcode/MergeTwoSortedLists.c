/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int val;
    struct Node *next;
}Node;

Node* createNode(int data){
    Node* newNode = (Node*)malloc(sizeof(Node));

    newNode -> val = data;
    newNode -> next = NULL;

    return newNode;
}

void printList(Node* head){
    Node* temp = head;

    while(temp){
        printf("%d ->", temp->val);
        temp = temp->next;
    }
    printf("Null\n");
}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    
}

int main(){
    Node* node1 = createNode(3);
    Node* node2 = createNode(1);
    Node* node3 = createNode(-5);


    node1->next = node2;
    node2->next = node3;


    printList(node1);

    free(node1);
    free(node2);
    free(node3);

    return 0;
}