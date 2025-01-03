import pathlib
import importlib.util

for path in pathlib.Path("solutions").glob("**/*.py"):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, "main"):
        year = path.parent.stem
        day = path.stem[-2:]
        input_file = pathlib.Path("inputs") / year / f"{day}.txt"
        with input_file.open() as f:
            data = f.read()
        part1, part2 = module.main(data.strip())
        print(f"{year}/{day}: {part1} {part2}")