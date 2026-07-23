class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        a = len(s)
        b = 0
        vowels  = 'aeiou'
        ans = 0
        count=0
        for i in range(a):
            if s[i] in vowels:
                count+=1

            if i-b+1 >  k:
                if s[b] in vowels:
                    count-=1
                b+=1
            if i-b+1 == k:
                ans = max(ans,count)
        return ans