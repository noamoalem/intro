
def return_k_subsets(n,k):

    if n < k or k < 0:
        return []
    if k == n:  # there is only one option
        #print(list(range(k)))
        return [list(range(k))]
    # recursive call for the function
    return return_k_subsets(n - 1, k) + [s + [n - 1] for s in return_k_subsets(n - 1, k - 1)]

print(return_k_subsets(3,2))
def fill_k_subsets(n, k, lst):
    if k <= n:
        cur_set = [False] * n
        fill_k_subset_helper(cur_set, k, 0, 0)



def print_set(cur_set):#,lst_of_all_combination = []):

   lst_of_one_combination = []
   for (idx, in_cur_set) in enumerate(cur_set):
       if in_cur_set:
           lst_of_one_combination.append(idx)
#   lst_of_all_combination.append(lst_of_one_combination)



def fill_k_subset_helper(cur_set, k, index, picked):#,lst):
   #lst_of_all_combination = []
   # Base: we picked out k items.
   if k == picked:
       print_set(cur_set)#,lst)
       return
   # If we reached the end of the list, backtrack.
   if index == len(cur_set):
       return
   # Runs on all sets that include this index.
   cur_set[index] = True
   fill_k_subset_helper(cur_set, k, index + 1, picked + 1)#,lst)
   # Runs on all sets that do not include index.
   cur_set[index] = False
   fill_k_subset_helper(cur_set, k, index + 1, picked)#,lst)


#print(fill_k_subsets(3,2,[]))







def print_k_subsets_helper(n, k):
    if n < k or k < 0:
        return []
    if k == n:  # there is only one option
        #print(list(range(k)))
        return [list(range(k))]
    # recursive call for the function
    return print_k_subsets_helper(n - 1, k) + [s + [n - 1] for s in print_k_subsets_helper(n - 1, k - 1)]

#print(print_k_subsets_helper(3, 2))

def print_k_subsets(n,k):
    lst_of_combination = print_k_subsets_helper(n, k)
    for i in lst_of_combination:
        print(i)

#print(print_k_subsets(3,2))