from tinydb import TinyDB
from tinydb.queries import Query
from redis import StrictRedis
from flask import current_app


class JsonDB(object):

    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.__project_table = self.db.table("project")

    @property
    def project_table(self):
        return self.__project_table

    def create_project(self, pname, gitaddr, redisdb, fsroot):
        self.__project_table.insert(
            {
                "pname": pname,
                "gitaddr": gitaddr,
                "redisdb": redisdb,
                "fsroot": fsroot
            }
        )

    def get_all_projects(self):
        return self.__project_table.all()

    def get_project_by_name(self, pname):
        query = Query()
        project = self.__project_table.get(query.name == pname)
        return project


class RedisManager(object):

    redis_dbconn_pool_by_project = {}

    def __init__(host, port):
        self.host = host
        self.port = port

    @classmethod
    def get_redis_connection(cls, project):
        """
            project = {
                "name":"fulishe",
                "redis_db":0
            }
        """
        pname = preject["name"]
        redis_db = int(project["redis_db"])
        redis_db_conn = None
        if pname in cls.redis_dbpool_by_project:
            redis_db_conn = cls.redis_dbconn_pool_by_project[pname]
        else:
            redis_config = current_app.config.redis_config
            try:
                redis_db_conn = StrictRedis(host=redis_config["host"],
                                            port=redis_config["port"],
                                            db=redis_db)
                cls.redis_dbconn_pool_by_project[pname] = redis_db_conn
            except Exception as e:
                print "Redis connect fail [%s]" % e

        return redis_db_conn
