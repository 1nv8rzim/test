#include <stdio.h>
#include <stdarg.h>

int max(int num1, int num2)
{
    if (num1 > num2)
    {
        printf("%d", num1);
    }
    else
    {
        printf("%d", num2);
    }
    return 0;
}

int main()
{
    while (1)
    {
        int num1, num2;
        printf("Enter Two Numbers: ");
        scanf("%d%d", &num1, &num2);
        max(num1, num2);
    }
}
