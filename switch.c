#include <stdio.h>

int main() {
    int number;
    
    printf("Enter a number (1-4): ");
    scanf("%d", &number);

    switch (number) {
        case 1:
            printf("B TECH CSE  m from amity university.\n");
            break;
	    case 2:
            printf("B TECH AIML.\n");
            break;
	    case 3:
            printf("B TECH ECE.\n");
            break;
	    case 4:
            printf("B TECH MECH.\n");
            break;
