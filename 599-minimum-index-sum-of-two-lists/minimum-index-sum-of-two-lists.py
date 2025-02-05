class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count_list1=Counter()
        count_list2= Counter()
        min_freq= float("inf")
        ans = []

        for i in range(len(list1)):

            count_list1[list1[i]] = i+1
        
        for i in range(len(list2)):

            count_list2[list2[i]] = i+1

        for  word in count_list1:

            if count_list2[word]   and  min_freq > (count_list1[word] + count_list2[word]):
                min_freq = count_list1[word] + count_list2[word]
        print(min_freq)
        
        for word in count_list1:

            if  count_list2[word]  and  count_list1[word] + count_list2[word] == min_freq:
                ans.append(word)
        
        return ans
        

        