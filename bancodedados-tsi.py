"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-14771.c308.sa-east-1-1.ec2.redns.redis-cloud.com',
    port=14771,
    decode_responses=True,
    username="default",
    password="nWfktsehkGEAzK0jCOU1ubaH1tUbUzlB",
)

r.set('chave', 10)
print(r.get('chave'))
if r.exists('chave'):
    r.incr('chave')
    print(r.get('chave'))
    r.incrby('chave', 5)
    print(r.get('chave'))
    r.decr('chave')
    print(r.get('chave'))
    r.decrby('chave', 3)
    print(r.get('chave'))
    r.delete('chave')
    print(r.exists('chaves'))
