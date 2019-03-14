#include <iostream>
#include "add.h"

using namespace std;
// int add_f(int a ,int b){
//     return a+b;
// }

int main(){
    int i = 0;
    i++;
    i++;
    i++;
    cout << "please input a num" << endl;
    cin >> i;
    i = add_f(1,i);
    cout << "i = " << i << endl;
    getchar();
    return 0;
}
