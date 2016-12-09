from db import RedisManager


def get_hit_set(project, fpath):
    redis_conn = RedisManager.get_redis_connection(project=project)
    key = fpath
    hits = redis_conn.smembers(key)
    return [int(x) for x in hits]
