import java.util.Scanner;
public class traversal {
    public static void main(String args[]){

        Scanner sc = new Scanner(System.in);
        // Simple Program
        System.out.println("Hello World");

        
        // Dynamic Initialization

        // int numbers[] = {1,2,3};
        // for(int i=0;i<3;i++){
        //     System.out.println(numbers[i]);
        // }

        // int numbers[] = new int[3];

        // for(int i=0;i<3;i++){
        //     numbers[i] = i;
        // }

        // for(int i=0;i<3;i++){
        //     System.out.println(numbers[i]);
        // }


        // Runtime Initialization

        int size = sc.nextInt();
        int numbers[] = new int[size];

        for(int i=0;i<size;i++){
            numbers[i] = sc.nextInt();
        }

        System.out.println("Numbers are : ");
        for(int i=0;i<size;i++){
            
            System.out.println(numbers[i]);
        }




    }
}
