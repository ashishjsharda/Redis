import redis
r=redis.Redis()
r.mset({"Employee1":"Jack","Employee2":"Jill"})
print(r.get("Employee1"))
