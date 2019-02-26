#!/usr/bin/env python3

# step 1: import the redis-py client package
import redis
import string
import random
import time
import datetime 

redis_host = "localhost"
redis_ports = [ 16379, 16380 ]
redismanager_port = 16381
redis_password = ""

def string_generator(size=19, chars=string.ascii_letters + string.digits):
    """Return random string"""
    return ''.join(random.choice(chars) for _ in range(size))

def date_diff_in_Seconds(dt2, dt1):
    """Get time delta between times in seconds"""
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds

def write_redis(redis_host, redis_port, redis_password, userid, msg):
    """Redis Write Program"""
   
    try:
        
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
   
        # Write message in Redis
        r.set(userid, msg)
   
    except Exception as e:
        print(e)

def read_redis(redis_host, redis_port, redis_password, userid):
    """Redis Read Function"""

    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        # step 5: Retrieve message from Redis
        msg = r.get(userid)

    except Exception as e:
        print(e)

    return msg


if __name__ == '__main__':
    userid = string_generator()
    t1 = datetime.datetime.now()
    write_redis(redis_host, redis_ports[0], redis_password, userid, str(t1))
    #random sleep interval
    time.sleep(random.randint(1,10))
    t2 = datetime.datetime.now()
    write_redis(redis_host, redis_ports[1], redis_password, userid, str(t2))
    delta =  date_diff_in_Seconds(t2, t1)
    write_redis(redis_host, redismanager_port, redis_password, userid, delta)
    print("For userid %s, time difference is %s seconds" % (userid, read_redis(redis_host, redismanager_port, redis_password, userid)))
