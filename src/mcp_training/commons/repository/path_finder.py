
from pathlib import Path



class PathFinder:

    @staticmethod
    def get_project_root():
        current_dir = Path(__file__).resolve()
        for parent in current_dir.parents:
            if (parent / ".gitignore").exists() or (parent / ".env").exists():
                return parent
        return current_dir.parent

    @staticmethod
    def get_data_root():
        return self.get_project_root() / "data"

    def get_all_paths(self):
        path_vault = {}
        data_root = self.get_data_root()
        for category_dir in data_root.glob("*"):
            if category_dir.is_dir():
                for json_file in category_dir.glob("*.json"):
                    key = f"{category_dir.name}/{json_file.name}"
                    path_vault[key] = json_file
        return path_vault





if __name__ == "__main__":
    root = PathFinder.get_project_root()
    print(f"📍 Project Root detected at: {root}")
    vault = PathFinder().get_all_paths()
    print(vault)