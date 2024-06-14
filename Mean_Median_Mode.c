#include<stdio.h>

int main() {
    printf("Enter how many numbers: ");
    int n;
    scanf("%d", &n);

    //intitalize an array to store the all value
    int arr[n];


    printf("Enter all the numbers one by one: ");
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    // Arithmatic mean calculation
    double sum = 0, arithmeticMean;
    for(int i = 0; i < n; i++) {
        sum += arr[i];
    }
    arithmeticMean = sum / n;
    printf("Arithmatic mean is: %lf\n", arithmeticMean);

    // Bubble sort for sorting the array
    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < n-i-1; j++) {
            if(arr[j] > arr[j+1]) {
                // Swap elements if the current element is greater than the next
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    // Median calculation
    float median;
    if(n % 2 == 0) { // If even number of elements
        median = (float)(arr[n / 2] + arr[n / 2 - 1]) / 2; // Determine median for even number of size n
    }
    else { // If odd number of elements
        median = arr[n / 2];
    }
    printf("Median is : %f\n", median);

    

    // Mode calculation
    int frequency[n]; // Array to store frequency of each number
    for(int i = 0; i < n; i++) {
        frequency[i] = -1; // Initialize frequency array
    }

    int maxFrequency = 0;
    int mode = -1; // Initialize mode to -1 indicating no mode found
    for(int i = 0; i < n; i++) {
        int count = 1;
        for(int j = i + 1; j < n; j++) {
            if(arr[i] == arr[j]) {
                count++;
                frequency[j] = 0; // Mark as counted
            }
        }
        if(frequency[i] != 0) {
            frequency[i] = count;
        }
        if(count > maxFrequency) {
            maxFrequency = count;
            mode = arr[i];
        }
    }

    if(maxFrequency > 1) {
        printf("Mode is: %d\n", mode);
    }
    else {
        printf("No mode found.\n");
    }

    return 0;
}
