package Linked_List;
import java.util.*;

public class Linkedlist_class {
    public static void main(String args[]){
        LinkedList<String> list = new LinkedList<String>();

        list.addFirst("a");
        list.addFirst("is");

        System.out.println(list);

        list.addLast("list");
        list.addFirst("This");
        System.out.println(list);

        System.out.println(list.size());

        // list.removeFirst();
        // list.removeLast();
        // list.remove(1);
        // System.out.println(list);

        for(int i=0;i<list.size();i++){
            System.out.print(list.get(i)+"->");
        }
        System.out.print("Null");
    }
}
