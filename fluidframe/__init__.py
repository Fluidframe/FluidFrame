from pathlib import Path

def get_lib_path() -> str:
    return Path(__file__).resolve().parent