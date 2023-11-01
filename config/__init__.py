import argparse
import pathlib
import tomllib

parser = argparse.ArgumentParser(description="Set environment for the script.")
parser.add_argument(
    "--prod", action="store_true", help="Set environment to production."
)
args = parser.parse_args()

filename = ".env.prod.toml" if args.prod else ".env.dev.toml"
path = pathlib.Path(__file__).parent / filename
with path.open(mode="rb") as fp:
    config = tomllib.load(fp)
