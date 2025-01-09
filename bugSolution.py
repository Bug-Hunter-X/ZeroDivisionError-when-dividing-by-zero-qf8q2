def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or handle the error in another way

result = function(10, 0) # result will be 0 now