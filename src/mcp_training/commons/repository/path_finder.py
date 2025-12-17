import logging
from pathlib import Path

logger = logging.getLogger("Path Finder")

class PathFinder:

    @staticmethod
    def get_data_root_path() -> Path:
        current_dir = Path(__file__).resolve()
        for parent in current_dir.parents:
            data_root = parent / "data"
            if data_root.exists():
                return data_root.resolve()
        return current_dir.resolve()

    def get_all_paths(self) -> dict:
        path_vault = {}
        data_root = self.get_data_root_path()

        if not data_root.exists():
            return {}

        for category in data_root.glob("*"):
            if category.is_dir():
                for file in category.glob("*.json"):
                    key = f"{category.name}/{file.name}"
                    path_vault[key] = file
        return dict(sorted(path_vault.items()))





if __name__ == "__main__":
    root = PathFinder.get_data_root_path()
    print(f"Project Root detected at: {root}")
    vault = PathFinder().get_all_paths()
    print(vault)