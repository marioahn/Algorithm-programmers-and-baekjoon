class Solution {
    public long solution(int price, int money, int count) {
        long cost = 0;
        
        for (int i=0; i<count+1; i++) {
            cost += price*i;
        }
        
        if (money < cost) return cost-money;
        else return 0;
            
    }
}