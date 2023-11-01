import pathlib
import tomllib

path = pathlib.Path(__file__).parent / ".env.dev.toml"
with path.open(mode="rb") as fp:
    config = tomllib.load(fp)
