#problem description:
    #given a random array, make it ordered.

#example:
    #[1,3,2,5,4] => [1,2,3,4,5]
    
#idea:
    #if the array contains n numbers, we traverse n-1 times and each time make a large number to the tail.
    #for each round, we compare the near two and make the larger one move behind.
    #for each round, we need to traverse based on index.
    #example: [1,3,2,5,4] there are 5 numbers, so we need 4 rounds. for first round, we compare from index=0 to index=4.....for last round, we compare from index=0 to index=1.

#code:
def bubble_sort(lst):
    for n in range(len(lst)-1,0,-1):
        for i in range(n):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst

#complexity:
#time complexity: O(n**2)
#space complexity: O(1)
