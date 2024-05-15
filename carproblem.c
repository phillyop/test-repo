#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to ask questions and return user input
char* askQuestion(const char* question) {
    printf("%s ", question);
    char* answer = (char*)malloc(100 * sizeof(char));
    scanf("%s", answer);
    return answer;
}

// Function to diagnose the car problem based on user input
void diagnoseProblem() {
    char* answer1 = askQuestion("Is the engine turning over? (yes/no)");
    char* answer2;
    char* answer3;
    char* answer4;

    if (strcmp(answer1, "yes") == 0) {
        answer2 = askQuestion("Does the engine start and then stall? (yes/no)");
        if (strcmp(answer2, "yes") == 0) {
            printf("Fuel delivery problem.\n");
        } else {
            answer3 = askQuestion("Does the engine not start at all? (yes/no)");
            if (strcmp(answer3, "yes") == 0) {
                printf("Battery or starter problem.\n");
            } else {
                printf("Invalid input.\n");
            }
            free(answer3);
        }
        free(answer2);
    } else if (strcmp(answer1, "no") == 0) {
        answer4 = askQuestion("Does the engine make any noise when turning the key? (yes/no)");
        if (strcmp(answer4, "yes") == 0) {
            printf("Starter or ignition problem.\n");
        } else {
            printf("Battery or connection problem.\n");
        }
        free(answer4);
    } else {
        printf("Invalid input.\n");
    }
    free(answer1);
}

int main() {
    diagnoseProblem();
    return 0;
}
