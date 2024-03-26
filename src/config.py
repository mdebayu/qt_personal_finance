"""Read the config file"""
from pathlib import Path
import tomllib

def get_cfg(path_to_cfg: str):
    """Read the Config File"""
    path = Path(path_to_cfg)
    if not path.exists():
        raise ValueError

    with open(path,"rb") as fr:
        return tomllib.load(fr)
