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
	    case 3:
            printf("You entered Three.\n");
            break;
	    case 4:
            printf("You entered Four.\n");
            break;
