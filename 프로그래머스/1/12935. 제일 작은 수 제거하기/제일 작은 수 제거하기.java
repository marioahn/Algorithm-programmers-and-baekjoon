import java.util.Arrays;
import java.util.stream.Stream;
// import java.util.List;
// import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        if (arr.length <= 1) return new int[]{ - 1}; // 아 이렇게 하면 되는구나;;
        int min = Arrays.stream(arr).min().getAsInt();
        return Arrays.stream(arr).filter(i -> i != min).toArray();
    }
}