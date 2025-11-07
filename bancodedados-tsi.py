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

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

