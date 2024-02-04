#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int GUESS(){
    int number, guess, nguesses=1;
    srand(time(0));

    // Generate a random number between 1 and 100
    number = rand()%100 + 1;

    do{
        printf("Guess the number between 1 to 100\n");
        scanf("%d", &guess);
        if (guess > number){
            printf("You guessed too high\n");
            printf("Guess again\n");
        }
        else if(guess < number){
            printf("You guessed too low\n");
            printf("Guess again\n");
        }
        else{
            printf("You guessed the number in %d att    empts\n", nguesses);
            printf("Congratulations\n");
        }
        nguesses++;
    }
    while (guess != number);
    return 0;
}