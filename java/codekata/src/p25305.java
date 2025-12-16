/*
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class p25305 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        List<Integer> x = new ArrayList<>();
        for (int i=0;i<n;i++) x.add(Integer.parseInt(st.nextToken()));
        x.sort(Collections.reverseOrder());
        System.out.println(x.get(k-1));
    }
}
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class HeapsortUtil{
    private static void heapify(int[] arr, int heapsize, int index){
        int largest = index;
        int left = 2*index+1;
        int right = 2*index+2;
        if (left < heapsize && arr[left] > arr[largest]) largest = left;
        if (right < heapsize && arr[right] > arr[largest]) largest = right;
        if (largest != index){
            int tmp = arr[largest];
            arr[largest] = arr[index];
            arr[index] = tmp;
            heapify(arr,heapsize,largest);
        }
    }

    static void sort(int[] arr){
        int n = arr.length;
        for (int i=n/2-1;i>-1;i--)
            heapify(arr,n,i);
        for (int i=n-1;i>0;i--){
            int tmp = arr[0];
            arr[0] = arr[i];
            arr[i] = tmp;
            heapify(arr,i,0);
        }
    }
}

public class p25305{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] x = new int[n];
        for (int i=0;i<n;i++) x[i] = Integer.parseInt(st.nextToken());
        HeapsortUtil.sort(x);
        for (int i=0;i<n;i++) System.out.print(x[i]+" ");
        System.out.println("\n"+x[n-k]);
    }
}