package Queue;

import java.util.*;

public class Simple_imp {
    public static void main(String args[]){
        Queue qu = new LinkedList<>();

        qu.add(1);
        qu.add(2);
        qu.add(3);

        System.out.println(qu);

        System.out.println("Element at top of the queue is : "+ qu.peek());

        qu.remove();

        System.out.println(qu);
    }
}