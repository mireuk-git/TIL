
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

class p14911{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> l = new ArrayList<>();
        while (st.hasMoreTokens()) {
            l.add(Integer.parseInt(st.nextToken()));
            
        }
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        l.sort(Comparator.naturalOrder());

        int left=0, right=l.size()-1;
        List<Integer[]> results = new ArrayList<>();
        while (left<right){
            int sum = l.get(left)+l.get(right);
            if (sum == n){
                Integer[] result = {l.get(left),l.get(right)};
                results.add(result);
                while (left < right && l.get(left).equals(result[0])) left++;
                while (left <right && l.get(right).equals(result[1])) right--;
            }
            else if (sum < n) left++;
            else right--;
        }

        for (Integer[] result : results){
            System.out.println(result[0]+" "+result[1]);
        }
        System.out.println(results.size());
    }
}