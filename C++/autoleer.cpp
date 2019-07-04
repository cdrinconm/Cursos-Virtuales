#include <iostream>
#include <fstream>
#include <stdio.h>

void lectura();

using namespace std;
int main(){
	lectura();
	return 0;
}

void lectura(){
	ifstream archivo;
	string texto;
	archivo.open("autoleer.cpp",ios::in);
	if (archivo.fail()){
		cout << "No se pudo abrir";
		exit(1);
	}
	while(!archivo.eof()){
		getline(archivo,texto);
		cout << texto << endl;
	}
	archivo.close();
}