using namespace std;
#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    string sortSentence(string s) {

        int prev_index = 0;
        vector<string> sentence(9, "");
        int i;
        int max_index = 0;
        for(i = 0; i < s.size(); i++) {
            char ch = s[i];
            if(ch == ' ') {
                int index = s[i-1] - '0';
                sentence[index-1] = s.substr(prev_index, i- prev_index - 1);
                prev_index = i+1;
                max_index = max(max_index, index);
            }

        }
        int index = s[s.size() - 1] - '0';
        sentence[index-1] = s.substr(prev_index, s.size() - prev_index - 1);
        max_index = max(max_index, index);

        string rtn_st;
        int j = 0;
        for(int j = 0; j < max_index; j++) {
            rtn_st += sentence[j];
            if (j < max_index - 1) {
                cout << max_index - 1 << endl;
                rtn_st += " ";
            }
        }

        return rtn_st;
    }
};
