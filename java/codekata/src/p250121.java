import java.util.Arrays;
import java.util.Map;

class Solution{
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by){
        Map<String,Integer> ColIndex = Map.of(
            "code",0,
            "date",1,
            "maximum",2,
            "remain",3
        );
        Arrays.sort(data,(a,b)->Integer.compare(a[ColIndex.get(ext)], b[ColIndex.get(ext)]));
        int i=0;
        while (data[i][ColIndex.get(ext)]<=val_ext) i++;
        int[][] view = Arrays.copyOfRange(data,0,i);
        Arrays.sort(view,(a,b)->Integer.compare(a[ColIndex.get(sort_by)], b[ColIndex.get(sort_by)]));
        return view;
    }
}


public class p250121 {
    
}
