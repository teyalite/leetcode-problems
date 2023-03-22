#include <stack>
#include <unordered_map>

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        std::unordered_map<char, char> map {{'}', '{'}, {')', '('}, {']', '['}};

        for(auto& c:s) {
            if (map.count(c) != 0) {
                if (stack.empty()) return false;

                auto t = stack.top();

                if (map[c] == t) {
                    stack.pop();
                } else {
                    stack.push(c);
                }
            } else {
                stack.push(c);
            }
        }
        
        return stack.empty();
    }
};