from pathlib import Path


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == "":
        return "Suffix is empty!"
    if not Path(path).exists():
        return "This path doesn't exist!"

    # rets = [str(item) for item in Path(path).glob('**/*' + suffix)]

    rets = []
    for item in Path(path).iterdir():
        if item.is_dir():
            ret = find_files(suffix, str(item))
            rets.extend(ret)
        else:
            if str(item).endswith(suffix):
                rets.append(str(item))
    return rets

if __name__ == "__main__":
    print(find_files('.c', './testdir'))
    print(find_files('', './testdir'))
    print(find_files('.c', './testdirdir'))