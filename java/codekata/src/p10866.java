
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Node {
    int value;
    Node next;
    Node prev;

    Node(int value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class Deque {
    Node head;
    Node tail;
    int size;

    Deque() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    void append(int value) {
        Node node = new Node(value);
        if (this.tail == null){
            this.head = this.tail = node;
        }
        else {
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
        }
        this.size+=1;
    }

    void appendleft(int value){
        Node node = new Node(value);
        if (this.head == null){
            this.tail = this.head = node;
        }
        else {
            this.head.prev = node;
            node.next = this.head;
            this.head = node;
        }
        this.size+=1;
    }

    int pop(){
        if (this.tail == null) { return -1; }
        int value = this.tail.value;
        this.tail = this.tail.prev;
        if (this.tail == null){
            this.head = null;
        }
        else {
            this.tail.next = null;
        }
        this.size-=1;
        return value;
    }

    int popleft() {
        if (this.head == null){ return -1; }
        int value = this.head.value;
        this.head = this.head.next;
        if (this.head==null) { this.tail=null; }
        else { this.head.prev=null; }
        this.size-=1;
        return value;
    }

    int size() {
        return this.size;
    }

    int empty() {
        if (this.size==0){ return 1; }
        else { return 0; }
    }

    int front() {
        if (this.head == null) { return -1; }
        return this.head.value;
    }

    int back() {
        if (this.tail == null) { return -1; }
        return this.tail.value;
    }
}

public class p10866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        Deque d = new Deque();
        for (int idx = 0; idx < n; idx++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            switch (command) {
                case "push_front":
                    {
                        int x = Integer.parseInt(st.nextToken());
                        d.appendleft(x);
                        break;
                    }
                case "push_back":
                    {
                        int x = Integer.parseInt(st.nextToken());
                        d.append(x);
                        break;
                    }
                case "pop_front":
                    System.out.println(d.popleft());
                    break;
                case "pop_back":
                    System.out.println(d.pop());
                    break;
                case "size":
                    System.out.println(d.size());
                    break;
                case "empty":
                    System.out.println(d.empty());
                    break;
                case "front":
                    System.out.println(d.front());
                    break;
                case "back":
                    System.out.println(d.back());
                    break;
                default:
                    break;
            }
        }
    }
}
