class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count_nums = Counter(nums)
        # res=[]
        
        
        # for i in count_nums:

        #     res.append([i,count_nums[i]])

        # res.sort(key=lambda x:x[1])

        # return [res[i][0] for i in range(len(res)-k,len(res))]


        count = defaultdict(int)
        maxx  = 0

        for num in  nums:
            count[num] += 1 
        maxx = max(count.values())
       
        
        buckets = [[] for i in range(maxx + 1)]
   

        for key, val in count.items():            
            buckets[val].append(key)
        print(buckets)

        count = 0
        ans = []
        buckets = buckets[:: - 1]

        for bucket in buckets:
           for val in bucket:

              if count < k:
                ans.append(val)
                count += 1

                

        return ans

            
        

        
        


         

        

        