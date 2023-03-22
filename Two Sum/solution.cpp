class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        std::vector<int> answer;

        for (int i = 0; i < nums.size(); ++i) {
            if (map.count(nums[i]) != 0) {
                answer.push_back(map[nums[i]]);
                answer.push_back(i);
                break;
            }
            
            map.insert(std::make_pair(target - nums[i], i));
        }
        
        return answer;
    }
};