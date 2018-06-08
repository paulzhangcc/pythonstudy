def consumer():
    r = ''
    while True:
        print('[CONSUMER] Consuming start')
        n = yield r
        if not n:
            print('[CONSUMER] Consuming start return')
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK===' + str(n)

def produce(c):
    c.send(None)
    n = 0
    while n < 2:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)