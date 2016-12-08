from tinydb import TinyDB
from tinydb.queries import Query


class DB(object):

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
        project = self.__project_table.get(query.name==pname)
        return project
