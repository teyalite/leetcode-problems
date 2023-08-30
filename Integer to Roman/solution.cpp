class Solution {
public:
    string intToRoman(int number) {
            std::vector<std::pair<int, std::string>> pairs = {{1000, "M"},
                                                  {900,  "CM"},
                                                  {500,  "D"},
                                                  {400,  "CD"},
                                                  {100,  "C"},
                                                  {90,   "XC"},
                                                  {50,   "L"},
                                                  {40,   "XL"},
                                                  {10,   "X"},
                                                  {9,    "IX"},
                                                  {5,    "V"},
                                                  {4,    "IV"},
                                                  {1,    "I"}};
    std::string roman;

    while (number > 0) {
        for (auto& pair : pairs) {
            if (number >= pair.first) {
                roman += pair.second;
                number -= pair.first;
                break;
            }
        }
    }

    return roman;
    }
};