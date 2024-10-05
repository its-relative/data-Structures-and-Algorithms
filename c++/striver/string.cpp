#include<bits/stdc++.h>

using namespace std;

int main(){
    // taking string as input

    string s1,s2;

    s1 = "Sapeksh";
    s2 = "Tomar";

    cin >> s1>>s2;
    cout<<s2<< ", "<< s1;
    return 0;
    

    // Now if we want to take the whole line
    //  instead of taking one 
    // string(before and after space) at a time

    string line;

    getline (cin, line);

    cout<< line;

    return 0;

    
    
    // Char

    char c;

    c = 'g'; //remember to put them in single quotes.

    cout<< c;
    return 0;

} 