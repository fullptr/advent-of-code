import pathlib
import importlib.util
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-y", "--year")
parser.add_argument("-d", "--day")
args = parser.parse_args()

for path in pathlib.Path("solutions").glob("**/*.py"):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, "main"):
        year = path.parent.stem
        day = path.stem[-2:]
        if (args.year is None or args.year == year) and (args.day is None or args.day == day):
            input_file = pathlib.Path("inputs") / year / f"{day}.txt"
            with input_file.open() as f:
                data = f.read()
            part1, part2 = module.main(data.strip())
            print(f"{year}/{day}:\n    1) {part1}\n    2) {part2}")