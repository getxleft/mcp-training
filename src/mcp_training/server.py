from mcp.server.fastmcp import FastMCP

from src.logs.logging_config import LoggingConfig

# Initialize the Server
mcp = FastMCP("Dungeon Master")

# ... Tools will go here next ...

if __name__ == "__main__":

    LoggingConfig.setup_logging()
