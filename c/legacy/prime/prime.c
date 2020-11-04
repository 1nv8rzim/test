#include <stdio.h>
#include <math.h>

int prime(int num)
{
    int flag = 1;
    for (int i = 0; i <= sqrt(num); ++i)
    {
        if (!(i % num))
        {
            flag = 0;
            break;
        }
    }
    return flag;
}

int main()
{
    int num;
    printf("Enter a number to see if prime: ");
    scanf("%d", &num);
    if (prime(num))
    {
        printf("%d is prime", num);
    }
    else
    {
        printf("%d is not prime", num);
    }
    return 0;
}