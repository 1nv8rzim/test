#include <stdio.h>
int array[10];

int main()
{
    for (int i = 0; i < 10; ++i)
    {
        array[i] = 10 - i;
    }

    for (int i = 0; i < 10; ++i)
    {
        printf("%d ", array[i]);
    }
    return 0;
}