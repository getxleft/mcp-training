import logging
from src.logs.logging_config import LoggingConfig
from src.utils import DataRepository

# 1. SETUP LOGGING
LoggingConfig.setup_logging()
logger = logging.getLogger("TestPilot")


def run_system_check():
    logger.info("🚀 --- STARTING REALITY CHECK ---")

    repo = DataRepository()
    TEST_DIR = "characters"
    TEST_FILE = "Setsuna"

    INITIAL_DATA = {
        "char_name": "Setsuna",
        "char_class": "Warrior",
        "char_hp": 25,
        "char_weapon": "Sword"
    }
    UPDATED_DATA = {"char_hp": 10}

    # --- NORMAL TESTS (Should be Green/White) ---

    # [TEST 1] CREATE
    logger.info(f"📝 [TEST 1] Creating {TEST_FILE}...")
    repo.create_data_file(TEST_DIR, TEST_FILE, INITIAL_DATA)
    logger.info("✅ Create executed.")

    # [TEST 2] READ
    logger.info(f"📖 [TEST 2] Verifying file...")
    read_data = repo.read_data_file(TEST_DIR, TEST_FILE)
    if read_data and read_data["char_weapon"] == "Sword":
        logger.info("✅ Read Verified.")

    # [TEST 3] UPDATE
    logger.info(f"💉 [TEST 3] Setsuna takes damage...")
    repo.update_data_file(TEST_DIR, TEST_FILE, UPDATED_DATA)
    logger.info("✅ Update executed.")

    # [TEST 4] BACKUP
    logger.info(f"🛡️ [TEST 4] Checking backup...")
    if repo.get_data_file(TEST_DIR, TEST_FILE).with_suffix(".json.bak").exists():
        logger.info("✅ Backup Found.")

    # [TEST 5] RESTORE
    logger.info(f"⏮️ [TEST 5] Restoring backup...")
    restored = repo.utilize_backup(TEST_DIR, TEST_FILE)
    if restored["char_hp"] == 25:
        logger.info("✅ Restore Successful (HP 25).")

    # ---------------------------------------------------------
    # 🧪 TEST 6: THE CRASH TEST (Should show YELLOW Warning)
    # ---------------------------------------------------------
    logger.info(f"\n🧪 [TEST 6] PROVOKING ERROR: Reading a Ghost File...")

    # We ask for "NonExistentGuy". This file does not exist.
    # Without the decorator, this would CRASH the script with FileNotFoundError.
    ghost = repo.read_data_file(TEST_DIR, "NonExistentGuy")

    if ghost is None:
        logger.info("✅ SHIELD HELD! The script did not crash. (Returned None)")
        logger.info("👀 ^ Look for the [MISSING] warning above.")
    else:
        logger.error("❌ Shield Failed (Something weird returned).")

    logger.info("🏁 --- CHECK COMPLETE ---")


if __name__ == "__main__":
    run_system_check()