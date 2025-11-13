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

class Usuario:
    def __init__(self, user_id, email, nome, senha):	
        self.user_id = user_id
        self.email = email
        self.nome = nome
        self.senha = senha

usuario = Usuario(1, "italo@gmail", "italo dantas", "12345")
print(usuario.nome, usuario.email, usuario.user_id, usuario.senha)


{
	'redis_version': '7.2.4',
	'uptime_in_seconds': 123456,
	'connected_clients': 10,
	'used_memory_human': '2.34M',
	'total_commands_processed': 150000,
	'role': 'master',
	'rdb_last_save_time': 1717000000,
	'aof_enabled': 1,
	'db0': {'keys': 25,'expires': 5, 'avg_ttl': 120000}
}

