/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* helper(ListNode* list1, ListNode* list2) {
        ListNode*  node = list1;

        while (node->next != nullptr && list2 != nullptr) {
            if (node->next->val  < list2->val) {
                node = node->next;
            } else {
                ListNode* tmp;
                tmp = node->next;
                node->next = list2;
                node = tmp;

                while (list2->next != nullptr && list2->next->val <= node->val) {
                    list2 = list2->next;
                }

                tmp = list2->next;
                list2->next = node;
                list2 = tmp;
            };
        }

        if (list2 != nullptr) {
            node->next = list2;
        }

        return list1;
    }

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == nullptr || list2 == nullptr) {
            return list1 == nullptr ? list2 : list1;
        }

        bool a = list1->val < list2->val;

        return helper( a ? list1 : list2, a ? list2 : list1);
    }


    ListNode* mergeTwoListsRecursiveSolution(ListNode* list1, ListNode* list2) {
        if (list1 == nullptr || list2 == nullptr) {
            return list1 == nullptr ? list2 : list1;
        }

        if (list1->val < list2->val) {
            list1->next = mergeTwoLists(list1->next, list2);
            return list1;
        } else {
            list2->next = mergeTwoLists(list1, list2->next);
            return list2;
        }
    }
};