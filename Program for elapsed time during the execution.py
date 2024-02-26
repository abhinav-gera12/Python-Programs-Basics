#Program for elapsed time during the execution

from timeit import default_timer as timer

starting_time = timer()

print("Hello World")        #write your code to check the time of execution

ending_time = timer()

print(ending_time - starting_time)