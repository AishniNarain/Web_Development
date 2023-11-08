import java.util.Scanner;

public class linear_search {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your number : ");
        int num = sc.nextInt();
        int flag = 0;
        int arr[] = {1,2,3,4,5,6,7};
        for(int i=0;i<7;i++){
            if(arr[i] == num){
                flag =1;
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
