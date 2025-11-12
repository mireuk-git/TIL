
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Cow{
    int id;
    Cow left;
    Cow right;

    public Cow(int id){
        this.id = id;
    }
}

class Line{
    Cow left;
    Cow right;
    int nextId = 0;
    
    public Line(){
        this.left = null;
        this.right = null;
    }

    public void addLeft(){
        this.nextId += 1;
        Cow newCow = new Cow(nextId);
        if (this.left == null){
            this.left = newCow;
            this.right = newCow;
        }
        else{
            this.left.left = newCow;
            newCow.right = this.left;
            this.left = newCow;
        }
    }

    public void addRight(){
        this.nextId += 1;
        Cow newCow = new Cow(nextId);
        if (this.right == null){
            this.right = newCow;
            this.left = newCow;
        }
        else{
            this.right.right = newCow;
            newCow.left = this.right;
            this.right = newCow;
        }
    }

    public void deleteLeft(){
        if (this.left == null) return;
        this.left = this.left.right;
        if (this.left==null) this.right = null;
        else this.left.left = null;
    }

    public void deleteRight(){
        if (this.right == null) return;
        this.right = this.right.left;
        if (this.right==null) this.left = null;
        else this.right.right = null;
    }

    public void print(){
        Cow curr = left;
        while (curr!=null){
            System.out.println(curr.id+" ");
            curr = curr.right;
        }
    }
}

public class p6119 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        Line line = new Line();
        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            String op = st.nextToken();
            String direction = st.nextToken();
            switch(op){
                case "A":
                    if (direction.equals("L")) line.addLeft();
                    else if (direction.equals("R")) line.addRight();
                    break;
                case "D":
                    int count = Integer.parseInt(st.nextToken());
                    if (direction.equals("L")) {
                        for (int j=0;j<count;j++) line.deleteLeft();
                    }
                    else if (direction.equals("R")) {
                        for (int j=0;j<count;j++) line.deleteRight();
                    }
                    break;
            }
        }
        line.print();
    }
}
