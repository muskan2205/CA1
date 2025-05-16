#include <stdio.h>

int main() {
    int number;
    
    printf("Enter a number (1-4): ");
    scanf("%d", &number);

    switch (number) {
        case 1:
            printf("You entered 200.\n");
            break;
	    case 2:
            printf("You entered 300.\n");
            break;
	    case 3:
            printf("You entered 400.\n");
            break;
	    case 4:
            printf("You entered 500.\n");
            break;
	    default:("invalid");
		    break;
