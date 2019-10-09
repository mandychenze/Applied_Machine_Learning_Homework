def fib(n):
    """
    :type N: int
    :rtype: int
    """   
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        res = [1,1]
        for i in range(2,n):
            res.append(res[-1]+res[-2])
        return res[-1]