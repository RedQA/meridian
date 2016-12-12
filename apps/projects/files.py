import os
import shutil
import codecs

from flask import current_app

exclude_dir_list = set([".git", ".idea", ".vscode"])

codetype_mapping = {
    ".sh": "shBrushBash.js",
    ".java": "shBrushJava.js",
    ".py": "shBrushPython.js",
    ".rb": "shBrushRuby.js",
    ".php": "shBrushPhp.js",
    ".css": "shBrushCss.js",
    ".js": "shBrushJScript.js",
    ".sql": "shBrushSql.js",
    ".xml": "shBrushXml.js"
}

codetype_alias = {
    ".sh": "bash",
    ".java": "java",
    ".py": "py",
    ".rb": "rb",
    ".php": "php",
    ".css": "css",
    ".js": "js",
    ".sql": "sql",
    ".xml": "xml"
}


def is_directory(project, fpath):
    split_fpath = []
    if fpath:
        split_fpath = fpath.split("/")
    path = os.path.join(project["fsroot"], *split_fpath)
    return os.path.isdir(path), path


def get_directory_structure(dpath, request_path=None):
    # ensure the suffix "/""
    request_path = request_path[
        :-1] if request_path.endswith("/") else request_path
    dpath = dpath[:-1] if dpath.endswith(os.path.sep) else dpath
    ret = {"dirs": [], "files": []}
    for root, dirs, files in os.walk(dpath):
        for _dir in dirs:
            if _dir not in exclude_dir_list:
                ret["dirs"].append({
                    "name": _dir,
                    "path": "/".join([request_path, _dir])
                })
        for _file in files:
            ret["files"].append({
                "name": _file,
                "path": "/".join([request_path, _file])
            })

        # jump out
        root = root[-1] if root.endswith(os.path.sep) else root
        if root == dpath:
            break
    return ret


def read_file_with_type(fpath):
    """
        return (content,codetype,codetype_js)
    """
    basename = os.path.basename(fpath)
    extname = os.path.splitext(basename)[1]
    if not extname or extname not in codetype_mapping:
        return None, None, None
    else:
        # solve the utf8 encodig problem
        f = codecs.open(fpath, mode='r', encoding="utf-8")
        content = f.read()
        return content, codetype_alias[extname], codetype_mapping[extname]
