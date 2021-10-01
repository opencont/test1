#include<stdio.h>
#include<stdlib.h>
struct TreeNode{
    int item;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* createNode(int value)
{
    struct TreeNode* newNode = malloc(sizeof(struct TreeNode));
    newNode->item = value;
    newNode->right = NULL;
    newNode->left = NULL;
    return newNode;
}
struct TreeNode *insertLeft(struct TreeNode* root, int data)
{
    root->left = createNode(data);
    return root->left;
}
struct TreeNode *insertRight(struct TreeNode* root, int data)
{
    root->right = createNode(data);
    return root->right;
}
void checkP(struct TreeNode* root, int a, int *p){
    if(root == NULL) return ;
    if(root->left && root->left->item == a ){
        *p = root->item;
    }else if(root->right && root->right->item == a){
        *p = root->item;
    }else{
        checkP(root->left, a, p);
        checkP(root->right, a, p);
    } 
}
void checkL(struct TreeNode* root, int a, int *l){
    if(root == NULL)return;
    if(root->item == a)return;
    checkL(root->left, a, l+1);
    checkL(root->right, a, l+1);
}
int areCousins(struct TreeNode* root, int a, int b){
    int p_a,p_b, l_a, l_b;
    p_a = -1;
    p_b = -1;
    l_a = -1;
    l_b = -1;
    checkP(root, a, &p_a);
    checkP(root, b, &p_b);
    checkL(root, a, &l_a);
    checkL(root, b, &l_b);
    if(p_a != p_b && l_a == l_b){
        return 1;
    }
    return 0;
        
}
void canBeMerged(struct TreeNode* root, int a, int b){
    if(areCousins(root, a, b)){  
        printf("True");
    }else{
        printf("False");
    }
}
int main()
{
    //Creating Tree with root
    struct TreeNode* root = createNode(1);
    
    //Inserting Nodes
    insertLeft(root, 2);
    insertRight(root, 3);
    insertLeft(root->left, 4);
    insertRight(root->left, 5);
    insertLeft(root->right, 6);
    insertRight(root->right, 7);
    insertRight(root->right->right, 8);
    canBeMerged(root, 2, 3);
   
    return 0;
}
