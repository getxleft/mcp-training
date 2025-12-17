import json
import logging
from pathlib import Path

from mcp_training.commons.repository.path_finder import PathFinder
from mcp_training.decorators.repo_error_handling import repo_error_handling

logger = logging.getLogger("Data Repository")

#TODO: advanced caching, async
class DataRepository:

    def __init__(self):
        self.path_finder = PathFinder() #singleton
        self.all_paths: dict[str, Path] = self.path_finder.get_all_paths()
        logger.info(f"Data Repository initialized. Number of Paths: {len(self.all_paths)} Available Paths: {self.all_paths}")

    def _refresh_cache(self) -> None:
        self.all_paths = self.path_finder.get_all_paths()
        logger.info("Path vault cache refreshed")

    @repo_error_handling
    def _data_path(self, directory: str, file: str) -> Path | None:
        return self.all_paths.get(f"{directory}/{file}")

    @repo_error_handling
    def read_data_file(self, directory: str, file: str) -> dict | None:
        path = self._data_path(directory, file)
        if not path or not path.exists():
            logger.warning(f"Could not read from: {path}, it does not exist")
            return None

        if path.stat().st_size == 0:
            logger.warning(f"File at {path} is empty. Returning empty dict.")
            return {}

        with open(path, "r") as f:
            logger.info(f"Successfully read from {path}")
            return json.load(f)

    @repo_error_handling
    def create_data_file(self, directory: str, file: str, data: dict) -> dict | None:
        base_data_dir = PathFinder().get_data_root_path()
        dir_path = base_data_dir / directory
        file_path = dir_path / f"{file}.json"

        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

        with open(file_path, "x") as f:
            json.dump(data or {}, f, indent=4)

        self._refresh_cache()
        logger.info(f"Successfully created data file with path {file_path}")
        return data


    @repo_error_handling
    def write_data_file(self, directory: str, file: str, data: dict) -> dict | None:
        path = self._data_path(directory, file)

        if not path:
            logger.warning(f"{path} does not exist. Can not write")
            return None

        self.backup_file(path)
        with open(path, "w") as f:
            json.dump(data or {}, f, indent=4)
            logger.debug(f"Successfully written to {path}")
        return data

    @repo_error_handling
    def update_data_file(self, directory: str, file: str, new_data: dict) -> dict | None:
        current_data = self.read_data_file(directory, file)
        data_path = self._data_path(directory, file)

        if current_data is None:
            logger.warning(f"{current_data} is empty. Can not recognize json.")
            return None

        if current_data == {}:
            return self.write_data_file(directory, file, new_data)

        current_data.update(new_data)
        logger.info(f"Successfully updated data file at {data_path}.")
        return self.write_data_file(directory, file, current_data)

    @staticmethod
    def backup_file(path: Path) -> None:
        backup_path = path.with_suffix(".json.bak")

        if path.exists():
            with open(path, "rb") as src, open(backup_path, "wb") as dst:
                dst.write(src.read())
                logger.info(f"Successfully backup file at {backup_path}")

if __name__ == "__main__":
    repo = DataRepository()
    repo.update_data_file("characters","setsuna.json",{"char_hp" : 9})
