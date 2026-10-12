#include<bits/stdc++.h>
using namespace std;

class Phone{
    public:
    Phone(){
        cout << "I am constructor\n";
    }
    void display(){
        cout << "I am method\n";
    }
    ~Phone(){
        cout << "I am destructor\n";
    }
};

int main(){
    Phone p;
    p.display();
    return 0;
}