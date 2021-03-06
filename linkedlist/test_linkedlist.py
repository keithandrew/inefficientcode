from linked_list import *

test_list = LinkedList()
test_list.build([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Test 1: build()")
test_list.list_print()
print(f"Current Node: {test_list.current_node}")
print("=" * 10)
print("Test 2: next()")
test_list.next()
print(f"Current Node: {test_list.current_node}")
print("=" * 10)
print("Test 3: previous()")
test_list.previous()
print(f"Current Node: {test_list.current_node}")
print("=" * 10)
print("Test 4: last_node()")
test_list.last_node()
print(f"Current Node: {test_list.current_node}")
print("=" * 10)
print("Test 5: reset()")
test_list.reset()
print(f"Current Node: {test_list.current_node}")
print("=" * 10)
print("Test 6: list_length()")
print(f"Number of Nodes: {test_list.list_length()}")
print("=" * 10)
print("Test 7: insert_node_after()")
test_list.insert_node_after(6, 22)
test_list.list_print()
print("=" * 10)
print("Test 8: insert_node_at()")
test_list.insert_node_at(3, 97)
test_list.list_print()
print("=" * 10)
print("Test 9: insert_node_at() - insert new head node")
test_list.insert_node_at(1, 63)
test_list.list_print()
print(f"Current head_node {test_list.head}")
print("=" * 10)
print("Test 10: insert_at_end()")
test_list.insert_at_end(57)
test_list.list_print()
print("=" * 10)
print("Test 11: replace_node()")
test_list.replace_node(9, 49)
test_list.list_print()
print("=" * 10)
print("Test 12: remove_node()")
test_list.remove_node(5)
test_list.list_print()
print("=" * 10)
print("Test 13: remove_node() - remove and reassign head node")
test_list.remove_node(1)
test_list.list_print()
print(f"Current head_node {test_list.head}")
print("=" * 10)
print("Test 14: locate()")
test_list.locate(6)
print(f"Current Node: {test_list.current_node}")
print("=" * 10)
print("Test 15: search()")
test_list.search(4)
print(f"Current Node: {test_list.current_node}")
print("=" * 10)
