"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia:
    The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
"""
def h_index(citations):
    h_ind = 0
    citations.sort(reverse=True)
    print(citations)
    for i in range(len(citations)):
        if citations[i] >= i+1:
            h_ind+=1
        else:
            break
    return h_ind



citations = [3,0,6,1,5]
# citations = [1,3,1]
print(h_index(citations))