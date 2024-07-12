#include "quicksort.h"


int main()
{
    int arr[] = {19, 17, 15, 12, 16, 18, 4, 11, 13};
    int n = sizeof(arr) / sizeof(arr[0]);

    // printing the original array
    printf("Original array: ");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    // calling quickSort() to sort the given array
    quickSort(arr, 0, n - 1);

    // printing the sorted array
    printf("\nSorted array: ");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    int arr_sorted_gold[] = {4, 11, 12, 13, 15, 16, 17, 18, 19};
    bool correct = true;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] != arr_sorted_gold[i])
        {
            correct = false;
            break;
        }
    }

    if (correct)
    {
        printf("\nTestbench passed!\n");
        return 0;
    }
    else
    {
        printf("\nTestbench failed!\n");
        return 1;
    }
}