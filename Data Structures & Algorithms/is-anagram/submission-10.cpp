#include <unordered_map>

class Solution {
public:
    unordered_map<char,int> inserting(string str){
        unordered_map<char,int> b = {};
        for (int i=0; i<str.length();i++){
            if(b.find(str[i]) == b.end()){
                b.insert({str[i],0});
            }
            else{
                b[str[i]] += 1;
            }
        }
        return b;
    }
    
    
    
    bool isAnagram(string s, string t) {
        return (inserting(t) == inserting(s));
    }
};
