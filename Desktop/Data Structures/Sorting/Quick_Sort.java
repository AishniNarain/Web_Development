package Sorting;

public class Quick_Sort {

    public static void printArray(int arr[]){
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }

    public static int partition(int arr[], int low, int high){
        int pivot = arr[high];
        int i = low - 1;

        for(int j=low;j<high;j++){
            if(arr[j] < pivot){
                i++;

                //swap
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        i++;
        int temp = arr[i];
        arr[i] = pivot;
        arr[high] = temp;
        return i;
    }

    public static void quick_sort(int arr[],int low, int high){
        if(low < high){
            int pidx = partition(arr,low,high);

            quick_sort(arr,low,pidx-1);
            quick_sort(arr, pidx+1, high);
        }
    }

    public static void main(String args[]){
        int arr[] = {6,3,9,5,2,8};
        int n = arr.length;

        System.out.println("Before Sorting : ");
        printArray(arr);

        quick_sort(arr, 0, n-1);

        System.out.println("After Quick Sort : ");
        printArray(arr);
}
}
