class Solution {
public:
    bool isAnagram(string s, string t) {
        char temp1[26]={0};
        if (s.length() != t.length()) return false;
        for(int i=0;i<s.length();i++)
        {
            temp1[s.at(i)-'a']++;
            temp1[t.at(i)-'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (temp1[i] != 0) 
                return false;
        }

        return true;
    }
};
