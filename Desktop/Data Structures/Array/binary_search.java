import java.util.Scanner;

public class binary_search {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number : ");
        int num = sc.nextInt();

        int arr[] = {1,2,3,4,5,6,7};
        int flag = 0;

        int low = 0;
        int high = arr.length -1 ;
        while(low<high){
            int mid = (low+high)/2;
            if(arr[mid] == num){
                flag = 1;
            }
            if(num < arr[mid]){
                high = high - 1;
            }
            else{
                low = low + 1;
            }
        }

        if(flag == 1){
            System.out.println("Number is present");
        }
        else{
            System.out.println("Number is not present");
        }


    }
}
