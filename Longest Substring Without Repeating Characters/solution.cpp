class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int index = 0, current_size = 0, size = 0;
        std::map<char, int> map;

        while (index < s.size()) {

            if (map.find(s[index]) != map.end()) {
                index = map[s[index]] + 1;
                map.clear();
                size = std::max(current_size, size);
                current_size = 0;
            } else {
                map[s[index]] = index;
                ++current_size;
                ++index;
            }
        }

        return std::max(size, current_size);
    }
};