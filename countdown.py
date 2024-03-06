"""Use a while-loop, and inside of the while-loop """
 
import time

sec=11
print(f"Starting to countdown from {sec} to 0")
start_time=time.time()
while sec >= 0:
    time.sleep(1)
    print(sec)
    sec-=1
end_time=time.time()
# print("Countdown is over!")
elapsed_time=end_time-start_time
print("Elapsed time for while-loop:",elapsed_time,"seconds")

####################################

start_time2=time.time()
for seconds in range(11,0,-1):
    time.sleep(1)
    print(seconds)   
end_time2=time.time()
elapsed_time2=end_time2-start_time2
print("Elapsed time of for-loop", elapsed_time2, "seconds")
# print (type(time), type(2))