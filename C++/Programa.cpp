#include <iostream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;
int main(){

	string p,q;
	int n;
	cin >> p;
	cin >> q;
	//cin >> n;
	cout << "Hola Mundo" << endl;	
	const char *command = p.c_str();
	const char *command2 = q.c_str();
	system(command);
	system(command2);

	return 0;
}