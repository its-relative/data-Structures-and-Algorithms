#include<bits/stdc++.h>

using namespace std;

int main() {
    int age;

    cin >> age;

    if(age > 18){
        cout<< "Adult";
    }

    else if(age == 18){
        cout << "Legally of age.";
    }

    else{
        cout <<"Kid";
    }
    return 0;
}