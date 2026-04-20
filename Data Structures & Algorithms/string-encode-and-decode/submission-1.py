class Solution:

    def encode(self, strs: List[str]) -> str:
        str="";
        for s in strs:
            str+=s;
            str+="."
        return str;

    def decode(self, s: str) -> List[str]:
        strs=[];
        st="";
        for i in s:
            if i==".":
                strs.append(st);
                st="";
                continue;
            st+=i;
        return strs;