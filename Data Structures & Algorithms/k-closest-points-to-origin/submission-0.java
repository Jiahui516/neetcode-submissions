class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> maxH=new PriorityQueue<>
        ((a,b)-> Integer.compare(b[0]*b[0]+b[1]*b[1],a[0]*a[0]+a[1]*a[1]));

        int[][] res = new int[k][2];
        for(int[] pt: points){
            maxH.offer(pt);
            if(maxH.size()>k) maxH.poll();
        }

        int i=0;
        while(maxH.size()>0){
            res[i++]=maxH.poll();
        }

        return res;
    }
}
