package Queue;

public class Array_imp {
    int front;
    int rear;
    int size;
    int [] queue;

    Array_imp(){
        front = -1;
        rear = -1;
        size = 10;
        queue = new int[size];
    }

    boolean isEmpty(){
        if(rear == -1){
            System.out.println("Queue is Empty");
        }
        return false;
    }


    int peek(){
        if(isEmpty()){
            System.out.println("Queue is Empty");
        }
        return queue[0];
    }

    void add(int data){
        if(rear == size-1){
            System.out.println("Queue is Full");
        }
        rear++;
        queue[rear] = data;
    }

    int remove(){
        if(isEmpty()){
            System.out.println("Queue is Empty");
        }
        front = queue[0];

        for(int i=0;i<rear;i++){
            queue[i] = queue[i+1];
        }

        rear--;
        return front;
    }

    
    
    public static void main(String args[]){
        Array_imp qu = new Array_imp();
        qu.add(1);
        qu.add(2);
        qu.add(3);
        qu.add(4);
        qu.add(5);
        System.out.println(qu.isEmpty());
        System.out.println(qu.peek());
        System.out.println(qu.remove());
        System.out.println(qu.remove());
        System.out.println(qu.remove());
        System.out.println(qu.remove());
        System.out.println(qu.isEmpty());
    }
}


