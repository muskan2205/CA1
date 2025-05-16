#include <stdio.h>

int main() {
    int number;
    
    printf("Enter a number (1-4): ");
    scanf("%d", &number);

    switch (number) {
        case 1:
            printf("You entered 20.\n");
            break;
	    case 2:
            printf("You entered 30.\n");
            break;
	    case 3:
            printf("You entered 40.\n");
            break;
	    case 4:
            printf("You entered 50.\n");
            break;
	    default:("invalid");
		    break;
