
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


class HeapSorter {
    private int[] A;
    private int n;
    private int count;
    private boolean stop;
    private int kLimit;

    private void printDebug(){
        System.out.print("count=" + count + " : ");
        for (int i=1; i<=n; i++) {
            System.out.print(A[i] + " ");
        }
        System.out.println();
    }

    public HeapSorter(int[] arr, int kLimit) {
        this.n = arr.length-1;
        this.A = new int[n+1];
        for (int i=0;i<=n;i++) { this.A[i] = arr[i]; }
        this.kLimit = kLimit;
        this.count = 0;
        this.stop = false;
    }

    public void heapify(int k, int size){
        if (this.stop) return;
        int left = 2*k, right = 2*k+1, smaller;
        if (right<=size){
            if (A[left]<A[right]){ smaller=left; }
            else { smaller=right; }
        }
        else if (left<=size) { smaller = left; }
        else return; 

        if (A[smaller]<A[k]){
            swap(k,smaller);
            count++;
            System.out.print("heapify: ");
            printDebug();
            if (count==kLimit){
                stop=true;
                return;
            }
            heapify(smaller,size);
        }

    }

    private void swap(int i, int j) {
        int tmp = A[i];
        A[i] = A[j];
        A[j] = tmp;
    }

    public void buildMinHeap(){
        for (int i=n/2;i>=1;i--){
            this.heapify(i,n);
        }
    }

    public void heapSort() {
        buildMinHeap();
        for (int i=n;i>=1;i--){
            if (stop) break;
            swap(1,i);
            count++;
            System.out.print("heapSort: ");
            printDebug();
            if (count==kLimit) {
                stop = true;
                break;
            }
            heapify(1,i-1);
        }
    }

    public void printArray() {
        if (count<kLimit) System.out.println(-1);
        else{
            for (int i=1;i<=n;i++){
                System.out.print(A[i]+" ");
            }
            System.out.println();
        }
    }
}

public class p24174 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int kLimit = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] A = new int[a+1];
        A[0] = 0;
        for (int i=1;i<=a;i++){
            A[i] = Integer.parseInt(st.nextToken());
        }
        HeapSorter hs = new HeapSorter(A,kLimit);
        hs.heapSort();
        hs.printArray();
        
    }
}
