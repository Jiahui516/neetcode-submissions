class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> max=new PriorityQueue<>((a,b)->b-a);
        for(int stone:stones){
            max.offer(stone);
        }
        while(max.size()>=1){
            if(max.size()==1) return max.peek();
            int remain = max.poll()-max.poll();
            if(remain>0) max.offer(remain);
        }
        return 0;
    }
}
