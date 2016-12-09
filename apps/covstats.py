from db import RedisManager


def get_hit_set(project, fpath):
    redis_conn = RedisManager.get_redis_connection(project=project)
