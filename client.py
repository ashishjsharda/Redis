import redis
r=redis.Redis(host="localhost",port=6379)
r.set('name','foo')
print(r.get('name'))
r.close()
