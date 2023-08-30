/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func normalize(node *ListNode, retenu int) int {
	node.Val += retenu
	retenu = node.Val / 10
	node.Val %= 10

	return retenu
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	node := &ListNode{Val: l1.Val + l2.Val}
	root := node
	retenu := root.Val / 10
	root.Val %= 10

	for l1.Next != nil && l2.Next != nil {
		node.Next = &ListNode{Val: l1.Next.Val + l2.Next.Val}
		node = node.Next
		retenu = normalize(node, retenu)

		l1 = l1.Next
		l2 = l2.Next
	}

	for l1.Next != nil {
		node.Next = &ListNode{Val: l1.Next.Val}
		node = node.Next
		retenu = normalize(node, retenu)
		l1 = l1.Next
	}

	for l2.Next != nil {
		node.Next = &ListNode{Val: l2.Next.Val}
		node = node.Next
		retenu = normalize(node, retenu)
		l2 = l2.Next
	}

	if retenu != 0 {
		node.Next = &ListNode{Val: retenu}
	}

	return root
}