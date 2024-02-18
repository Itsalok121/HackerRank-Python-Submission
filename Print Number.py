'''
without using a string function print numbers upto the integer which is given as an input.

'''
if __name__ == '__main__':
    n = int(input())
    nums = [num for num in range(1,n+1)]
    
    for i in nums:
        print(i, end = '')
