#include <stdio.h>
#include <omp.h>

// Calculate a*a + b*b - 4ac
int main()
{
    int ID, a = 5, b = 5, result = 0, result1 = 0, result2 = 0, result3 = 0, result4 = 0;
	#pragma omp parallel
	{
		ID = omp_get_thread_num();
        printf("ID: %d\n", ID);
        switch (ID+1)
        {
        case 1:
            result1 = a * a;
            printf("First0: %d\n", result1);
            break;

        case 2:
            result2 = b * b;
            printf("First1: %d\n", result2);
            break;

        case 3:
            result3 = 4 * a * b;
            printf("First2: %d\n", result3);
            break;

        case 4:
            result4 = b * b * b;
            printf("First3: %d\n", result4);
            break;
        
        default:
            break;
        }
	}
    printf("SECOND:\nResult1: %d\nResult2: %d\nResult3: %d\nResult4: %d\n", result1, result2, result3, result4);
    result = result1 + result2 - result3 + result4;
    printf("Result: %ud\n", result);
	return 0;
}
