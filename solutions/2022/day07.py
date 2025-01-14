from collections import defaultdict, namedtuple
from pathlib import Path

File = namedtuple("File", ["name", "size"])
Filesystem = dict[Path, list[Path | File]]

def get_dirsize(dirname: Path, fs: Filesystem):
    dirsize = 0
    for file in fs[dirname]:
        match file:
            case File(_, size):
                dirsize += size
            case Path as p:
                dirsize += get_dirsize(p, fs)
    return dirsize

def main(data):
    current_path = Path("/")
    fs: dict[Path, list[Path | File]] = defaultdict(list)

    for line in data.split("\n"):
        match line.split():
            case ["$", "cd", "/"]:
                current_path = Path("/")
            case ["$", "cd", ".."]:
                current_path = current_path.parent
            case ["$", "cd", dirname]:
                current_path = current_path / dirname
            case ["$", "ls"]:
                pass
            case ["dir", subdir]:
                fs[current_path].append(current_path / subdir)
            case [size, file] if size.isdigit():
                fs[current_path].append(File(name=file, size=int(size)))

    unused_space = 70000000 - get_dirsize(Path("/"), fs)
    space_to_free = 30000000 - unused_space

    part1 = 0
    part2 = float("inf")
    for directory, files in fs.items():
        size = get_dirsize(directory, fs)
        if size <= 100000:
            part1 += size
        if space_to_free <= size < part2:
            part2 = size

    return part1, part2