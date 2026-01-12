#include <iostream>
#include <string>
#include <vector>
using namespace std;


int main(void) {
	string input;
	cin >> input;

	int correct = 0;
	int result = 0;

	if (input.length() % 2 != 0) {
		input.erase(input.length() / 2, 1);
	}

	for (int i = 0; i < input.length()/2; i++) {
		if (input[i] == input[input.length() -1 -i]) {
			correct += 1;
		}
		else
			break;
	}

	if (correct == input.length() / 2)
		result = 1;

	cout << result;

	return 0;

	
}
