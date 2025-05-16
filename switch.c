#include <stdio.h>

int main() {
    int number;
    
    printf("Enter a number (1-4): ");
    scanf("%d", &number);

    switch (number) {
        case 1:
            printf("You entered 2000.\n");
            break;
	    case 2:
            printf("You entered 3000.\n");
            break;
	    case 3:
            printf("You entered 4000.\n");
            break;
	    case 4:
            printf("You entered 5000.\n");
            break;
	    default:("invalid");
		    break;
