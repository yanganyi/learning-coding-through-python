

num_list = [1,2,9,8,5]

# list has a built-in sort() function
# num_list.sort(reverse=True)
# print(num_list)


# time complexity: O(n^2)
def my_sort(oldlist):
    newlist = []
    while len(oldlist)>0:
        n = oldlist[0]
        insert_pos = len(newlist)
        for i,v in enumerate(newlist):
            if n < v:
                insert_pos = i
                break
        newlist.insert(insert_pos,n)
        oldlist.pop(0)
    return newlist

# time complexity: O(n^2)
# def my_sort(oldlist):
#     newlist = []
#     while len(oldlist)>0:
#         n = oldlist[0]
#         found = False
#         for i,v in enumerate(newlist):
#             if n < v:
#                 newlist.insert(i,n)
#                 found = True
#                 break
#         if not found:
#             newlist.append(n)
#         oldlist.pop(0)
#     return newlist


def mergeSort(list):
    if len(list)<=1:
        return list

    mid = len(list) // 2 #Finding the mid of the array
    left_list = list[:mid] # Dividing the array elements
    right_list = list[mid:] # into 2 halves

    left_list = mergeSort(left_list) # Sorting the first half
    right_list = mergeSort(right_list) # Sorting the second half

    return merge_two_lists(left_list, right_list)


def merge_two_lists(left_list, right_list):

    merged_list = []
    i = j = 0

    # every iteration, we merge the min of two sublists into the merged list
    # until one of the sublists is empty
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1

    # continue to copy over all the remaining numbers in the sublists
    while i < len(left_list):
        merged_list.append(left_list[i])
        i += 1

    while j < len(right_list):
        merged_list.append(right_list[j])
        j += 1

    # return the merged list
    return merged_list


print(mergeSort(num_list))
