# profiling_dectorator
## This decorator mimics behavior of the timeit method used in Command-Line Interface.

## **Features**
* The decorator can be used with keyword arugment *number* to specify the number of loops, or without argument like a normal decorator.
* The return statement of the function to be measured will not be disrupted.
* Same to using timeit in cli, the shortest execution time will be reported instead of the cumulative execution time.
* The unit (sec, msec, usec) of the execution time will be adjusted accordingly for easy interpretation. 

## **Example**
```python
  @cli_timeit                 # uasd without argument
  def foo():
      return "-".join(map(str, range(100)))

  @cli_timeit(number=10000)   # uasd with argument
  def bar():
      return "-".join(map(str, range(100)))
        
  foo()  # 1000 loops, best of 3: 15.020 usec per loop
  bar()  # 10000 loops, best of 3: 15.199 usec per loop
```
