#include <iostream>
#include <unordered_map>
#include <list>
#include <vector>
#include <stdlib.h>
#include <time.h>


using namespace std;

class TreapTree{

	struct Node{
		Node *left;
		Node *right;
		int val;
		int count=1;
		int priority;
		
		Node(Node* l, Node *r,int v,int p): left(l),right(r),val(v),priority(p) {
		}
	};
	Node* nullNode;
	Node* root;
	
	
	void insert(int x, Node* &t){
		if(t==nullNode)	{
			t = new Node(nullNode,nullNode,x,rand());
		}else{
			if(t->val == x){
				t->count +=1;
			}else if(x<t->val){
				insert(x,t->left);
				if(t->left->priority<t->priority)
					rotateWithLeft(t);
			}else {
				insert(x,t->right);
				if(t->right->priority<t->priority)
					rotateWithRight(t);
			}
		}
	}
		
	void remove(int x,Node* &t){
		if(t!=nullNode){
			if(x<t->val){
				remove(x,t->left);
			}else if(x>t->val){
				remove(x,t->right);
			}else{
				if(t->count>1){
					t->count -= 1;
				}else{
					if(t->left->priority<t->right->priority){
						rotateWithLeft(t);
					}else{
						rotateWithRight(t);
					}
					
					if(t!=nullNode){
						remove(x,t);
					}else{
						delete t->left;
						t->left = nullNode;
					}
				}
			}
		}
	}
	
	void rotateWithLeft(Node* &t){
		Node *l = t->left;
		t->left = l->right;
		l->right = t;
		t = l;
	}
	
	void rotateWithRight(Node* &t){
		Node *r = t->right;
		t->right = r->left;
		r->left = t;
		t = r;
	}
	
	void print(Node* t,string s){
		if(t==nullNode)
			return ;
		print(t->left,s+"\t");
		cout<<s<<t->val<<","<<t->count<<endl;
		print(t->right,s+"\t");
	}
	
public:	
	TreapTree(){
		nullNode = new Node(NULL,NULL,0,INT_MAX);
		nullNode->left = nullNode->right = nullNode;
		root = nullNode;
	}
	void insert(int x){
		insert(x,root);
	}
	
	void remove(int x){
		remove(x,root);
	}
	
	void print(){
		print(root,"");
	}
	
	
};

/*
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        
    }
};*/

int main(){
	srand(time(NULL));
	
	int arr[] = {5,7,2,6,7,9,10,1,5,6,7,3,9};
	int n = sizeof(arr)/sizeof(arr[0]);
	TreapTree tree;
	for(int i=0;i<n;++i){
		tree.insert(arr[i]);
	}
	tree.print();
	
	tree.remove(5);
	tree.print();
	tree.remove(5);
	tree.print();
	tree.remove(3);
	tree.print();
	return 0;
}