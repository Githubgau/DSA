class Solution(object):
    def romanToInt(self, a):
        l={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s=0
        i=0
        while i<len(a):
            if i!=(len(a)-1) and l[a[i]]<l[a[i+1]]:
                s=s+(l[a[i+1]]-l[a[i]])
                i=i+1
            else:
                s=s+l[a[i]]
            i=i+1
        return (s)
        """
        :type s: str
        :rtype: int
        """
        