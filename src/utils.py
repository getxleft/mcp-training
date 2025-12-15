import json
from pathlib import Path

from src.decorators.repo_error_handling import repo_error_handling, logger
from src.logs.logging_config import LoggingConfig


#temp with campaign.json and maybe active players so data is in cache
#base repository template
#if 2 users update at the same times we lose data (async)

class DataRepository:

    def __init__(self):
        self.BASE_DIR = Path(__file__).parent.parent.resolve()
        self.DATA_DIR: Path = (self.BASE_DIR / "data").resolve()
        logger.info(f"DataRepository initialized. Root: {self.DATA_DIR}")

    def get_data_file(self,dir_name: str, file_name: str) -> Path:
        return (self.DATA_DIR/ f"{dir_name}" / f"{file_name}.json").resolve()

    @repo_error_handling
    def get_data_vault(self) -> dict | None:
        data_vault = {}
        for dir_name in [data_dirs.name for data_dirs in self.DATA_DIR.glob("*")]:
            file_name = [data_files.name for data_files in (self.DATA_DIR / f"{dir_name}").glob("*.json")]
            data_vault[dir_name]= file_name
        return data_vault

    @repo_error_handling
    def read_data_file(self, dir_name: str, file_name: str) -> dict | None:
        with open(self.get_data_file(dir_name, file_name), "r") as f:
            return json.load(f)

    @repo_error_handling
    def write_data_file(self, dir_name: str, file_name: str, data: dict) -> dict | None:
        data_path = self.get_data_file(dir_name, file_name)
        self.backup_file(data_path)
        with open(data_path, "w") as f:
            json.dump(data, f, indent=4)
            return data

    @repo_error_handling
    def create_data_file(self, dir_name: str, new_file_name: str, data: dict) -> dict | None:
        with open(self.get_data_file(dir_name,new_file_name), "w") as f:
            json.dump(data, f, indent=4)
            return data

    @repo_error_handling
    def print_data_file(self, dir_name: str, file_name: str) -> dict | None:
        data = self.read_data_file(dir_name, file_name)
        for k, v in data.items():
            print(f"{k}: {v}")

    @repo_error_handling
    def update_data_file(self, dir_name: str, file_name: str, new_data: dict) -> dict | None:
        current_data = self.read_data_file(dir_name, file_name)
        if current_data is not None:
            current_data.update(new_data)
            self.write_data_file(dir_name, file_name, current_data)
            return current_data
        else:
            return self.create_data_file(dir_name, file_name, new_data)

    @repo_error_handling
    def utilize_backup(self, dir_name, file_name) -> dict | None:
        original_path = (self.get_data_file(dir_name, file_name))
        backup_path = original_path.with_suffix(".json.bak")
        with open(backup_path, "r") as f:
            backup_data = json.load(f)
            self.write_data_file(dir_name, file_name, backup_data)
            return backup_data

    @staticmethod
    def backup_file(data_path: Path):
        backup_path = data_path.with_suffix(".json.bak")
        if data_path.exists():
            with open(data_path, "rb") as src, open(backup_path, "wb") as dst:
                dst.write(src.read())


if __name__ == "__main__":
    repo = DataRepository()
    LoggingConfig.setup_logging()
