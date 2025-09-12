import java.util.Scanner;
import java.util.TreeSet;
class Pair implements Comparable<Pair>{
    int diff1;
    int diff2;
    
    Pair(int diff1, int diff2) {
        this.diff1 = diff1;
        this.diff2 = diff2;
    }

    @Override
    public int compareTo(Pair o) {
        if (this.diff1 != o.diff1) return this.diff1 - o.diff1;
        return this.diff2 - o.diff2;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Pair)) return false;
        Pair other = (Pair) obj;
        return this.diff1 == other.diff1 && this.diff2 == other.diff2;
    }

    @Override
    public int hashCode() {
        return 31 * diff1 + diff2;
    }

    @Override
    public String toString() {
        return diff1 + " " + diff2;
    }
}

public class p29808 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int s = scanner.nextInt();
        TreeSet<Pair> p = new TreeSet<>();
        if (s%4763==0){
            s/=4763;
            int[] X = {508,108};
            int[] Y = {305,212};

            for (int diff1=0;diff1<200;diff1++) {
                for (int x:X) {
                    for (int y:Y) {
                        long remain = s-(diff1*x);
                        if (remain%y==0){
                            int diff2=(int)(remain/y);
                            if (diff2>=0 && diff2<=200){
                                p.add(new Pair(diff1,diff2));
                            }
                        }
                    }
                }
            }
        }
        System.out.println(p.size());
        for (Pair pair: p) {
            System.out.println(pair);
        }
    }
}
