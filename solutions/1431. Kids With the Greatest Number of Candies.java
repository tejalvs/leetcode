class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int total=0;
        int max=0;
        List<Boolean> check=new ArrayList<Boolean>();
        for(int i=0;i<candies.length;i++)
        {
             if(candies[i]>max)
                max=candies[i];
            }
        for(int i=0;i<candies.length;i++)
        {   
             if(candies[i]+extraCandies>=max)
                check.add(true);
             else
                 check.add(false);
            }
        return check;
    }
}
