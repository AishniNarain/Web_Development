package Sorting;
import java.util.*;

public class Bucket_Sort {

    public static void bucket_sort(float arr[],int n){
        if(n<=0){
            return;
        }

        Vector<Float>[] bucket = new Vector[n];

        for(int i=0;i<n;i++){
            bucket[i] = new Vector<Float>();
        }

        for(int i=0;i<n;i++){
            int idx = (int) arr[i]*n;
            
            bucket[idx].add(arr[i]);
        }

        for(int i=0;i<n;i++){
            Collections.sort(bucket[i]);
        }

        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < bucket[i].size(); j++) {
                arr[index++] = bucket[i].get(j);
            }
        }
    }
    public static void main(String args[]){
        float arr[] = { (float)0.897, (float)0.565,
                        (float)0.656, (float)0.1234,
                        (float)0.665, (float)0.3434 };

        int n = arr.length;
        bucket_sort(arr, n);

        System.out.println("Sorted array is ");
        for (float el : arr) {
        System.out.print(el + " ");
        }
    }
}
