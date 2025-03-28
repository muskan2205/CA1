#include <stdio.h>

int main() {
    int number;
    
    printf("Enter a number (1-4): ");
    scanf("%d", &number);

    switch (number) {
        case 1:
            printf("You entered One.\n");
            break;
	    case 2:
            printf("You entered Two.\n");
            break;
