import redis
# from redis import Connection

connectionPoolConfig = redis.ConnectionPool()
connectionPoolConfig.max_connections=10
pool = redis.Redis(connection_pool=connectionPoolConfig)

pool.sadd("zjf",123)

result = pool.smembers("zjf")
for data in result:
    str = 'type={},data={}'
    print(str.format(type(data), data))