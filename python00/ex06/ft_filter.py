def ft_filter(function, iterator):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    
    for item in iterator:
        if function(item):
            yield item 
            
if __name__ == "__main__": 
    print(filter.__doc__)
    print("\n")
    print(ft_filter.__doc__)

    print(next(filter(lambda x: x % 2 == 0, range(10))))
    print(next(ft_filter(lambda x: x % 2 == 0, range(10))))