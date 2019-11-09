#include <stdio.h>
#include <omp.h>

int main() {
    #pragma omp parallel for
    for (int i = 0; i < 10; i++) {
        printf("Hello World from %d, %d\n", omp_get_thread_num()                               ,i);
    }
    return 0;
}