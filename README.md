# 实时代码覆盖率收集和显示

## 系统组件

1. Client
* 定制版的coverage.py，实时把coverage数据传输到redis存储中

2. Meridian
* 从redis读取coverage的数据，并结合最新的gitlab代码+syntaxHighLight来做web端的展现

## Meridian 设计

* ### Database schema design

Project Schema
``` json
{
    "project_name": "fulishe",
    "git": "https://gitlab.xiaohongshu.com/red-qa/meridian.git",
    "redis_db": "0",
    "fs_root": "/repository/fulishe"
}
```

* ### URL Definition

项目信息相关

```
GET /projects
GET /projects/{project_name}
```

项目文件列表

```
GET /projects/{project_name}/tree
GET /projects/{project_name/tree/{file|folder path}}
```
