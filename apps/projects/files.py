import os
from flask import current_app

exclude_dir_list = set([".git", ".idea", ".vscode"])


def is_directory(project, fpath):
    print project
    split_fpath = []
    if fpath:
        split_fpath = fpath.split("/")
    path = os.path.join(project["project_root"], *split_fpath)
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


def read_file(fpath):
    pass
