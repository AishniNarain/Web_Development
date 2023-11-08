import java.util.*;

public class Simple_imp {
    public static void main(String args[]){
        Stack st1 = new Stack<>();

        st1.push(1);
        st1.push(2);
        st1.push(3);

        System.out.println(st1);

        System.out.println("Element at top of the stack is : "+ st1.peek());

        st1.pop();

        System.out.println(st1);
    }
}