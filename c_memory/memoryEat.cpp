#include <stdio.h>
#include <stdlib.h>

unsigned long long memory_to_eat = 1024 * 50000;
size_t eaten_memory = 0;
void *memory = NULL;

int eat_kilobyte()
{
    if (memory == NULL)
        memory = malloc(1024);
    else
        memory = realloc(memory, (eaten_memory * 1024) + 1024);
    if (memory == NULL)
    {
        return 1;
    }
    else
    {
        //Force the kernel to map the containing memory page.
        ((char*)memory)[1024*eaten_memory] = 42;

        eaten_memory++;
        return 0;
    }
}

int main(int argc, char **argv)
{
    printf("I will try to eat %i kb of ram\n", memory_to_eat);
    int megabyte = 0;
    while (memory_to_eat > 0)
    {
        memory_to_eat--;
        if (eat_kilobyte())
        {
            printf("Failed to allocate more memory! Stucked at %i kb :(\n", eaten_memory);
            return 200;
        }
        if (megabyte++ >= 1024)
        {
            printf("Eaten 1 MB of ram\n");
            megabyte = 0;
        }
    }
    printf("Successfully eaten requested memory!\n");
    free(memory);
    return 0;
}