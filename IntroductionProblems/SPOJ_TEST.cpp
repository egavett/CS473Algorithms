#include <iostream>
#include <stdio.h>
using namespace std;
 
int main() {
	// your code goes here
	
	bool found = false;
	int value;
	
	while (!found) {
		scanf("%d", &value); 
		
		if (value == 42) {
			found = true;
		} else {
			cout << value << endl;
		}
	}
	
	return 0;
} 