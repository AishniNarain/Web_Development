package Linked_List;



public class Simple_imp {
    Node head;
    int size;

    Simple_imp(){
        this.size = 0;
    }

    class Node{
        int data;
        Node next;
    

    Node(int data){
        this.data = data;
        this.next = null;
        size++;
    }
    }

    
    public void addFirst(int data){
        Node newnode = new Node(data);
        if(head == null){
            head = newnode;
            return;
        }
        newnode.next = head;
        head = newnode;
    }

    public void addLast(int data){
        Node newnode = new Node(data);
        if(head == null){
            head = newnode;
            return;
        }
        Node currnode = head;
        while(currnode.next != null){
            currnode = currnode.next;
        }
        currnode.next = newnode;
    }

    public void deleteFirst(){
        if(head == null){
            System.out.println("List is empty");
            return;
        }
        size--;
        head = head.next;
    }

    void deleteLast(){
        if(head == null){
            System.out.println("List is empty");
            return;
        }
        size--;
        if(head.next == null){
            head = null;
        }

        Node secondLast = head;
        Node lastNode = head.next;

        while(lastNode.next != null){
            lastNode = lastNode.next;
            secondLast = secondLast.next;
        }
        secondLast.next = null;
    }

    public int getSize(){
        return size;
    }

    public void printList(){
        if(head == null){
            System.out.println("Linked List is empty");
            return;
        }
        Node currnode = head;
        while(currnode != null){
            System.out.print(currnode.data+"->");
            currnode = currnode.next;
        }
        System.out.println("Null");
    }
    public static void main(String args[]){
        Simple_imp list= new Simple_imp();
        list.addFirst(2);
        list.addFirst(1);
        // list.printList();

        list.addLast(3);
        list.addLast(4);
        list.printList();

        list.deleteFirst();
        list.printList();

        list.deleteLast();
        list.printList();

        System.out.println(list.getSize());
    }

}
