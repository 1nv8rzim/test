#include <stdio.h>

int factorial(int num)
{
    if (num == 0)
    {
        return 1;
    }
    else
    {
        return num * factorial(num - 1);
    }
}

int main()
{
    int input;
    printf("Enter Number: ");
    scanf("%d", &input);
    printf("%d", factorial(input));
    return 0;
}