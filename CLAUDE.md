# CLAUDE.md - Project Context & Memory

> **Last Updated:** 2025-12-19
> **Project Status:** Early Development - Infrastructure Complete, Core MCP Functionality Pending

---

## Project Overview

### What This Project Is
**Dungeon Master MCP Server** - A Model Context Protocol (MCP) implementation themed around a D&D-style game system. This server enables Claude (or other AI assistants) to manage tabletop RPG game state through structured tools and commands.

### Project Goals
1. **Learn MCP Protocol** - Understand how to build MCP servers that extend Claude's capabilities
2. **Learn Industry-Standard Patterns** - Implement Repository Pattern, Service Layer, Managed Services
3. **Build Production-Ready Code** - Error handling, logging, testing, proper architecture
4. **Create Functional Game System** - Character management, enemy tracking, campaign state, inventory

### Current Phase
**Phase 0: Infrastructure Complete, Core Implementation Pending**
- Data repository layer: ✅ Complete
- Error handling: ✅ Complete
- Logging: ✅ Complete
- Service framework: ✅ Infrastructure only (no implementations)
- Domain models: ⚠️ Minimal (1 character class, 1 enemy type)
- MCP Server: ❌ Skeleton only (12 lines)
- MCP Tools: ❌ Not implemented (`tools.py` is empty)
- Tests: ❌ Deleted in last commit

---

## Architecture & Logic

### Directory Structure
```
mcppractice/
├── data/                          # JSON data storage
│   ├── campaign/                 # Campaign state files
│   ├── characters/               # Player character files
│   └── enemies/                  # Enemy/NPC files
│
├── src/mcp_training/
│   ├── server.py                 # Main MCP server entry point
│   ├── tools.py                  # MCP tools (EMPTY - needs implementation)
│   │
│   ├── commons/                  # Shared utilities
│   │   ├── repository/
│   │   │   ├── data_repository.py      # CRUD operations for JSON files
│   │   │   └── path_finder.py          # Automatic file discovery
│   │   └── service/
│   │       ├── initialization_order.py  # Service startup ordering
│   │       ├── shutdown_order.py        # Service shutdown ordering
│   │       └── service_status.py        # Service state enum
│   │
│   ├── core/
│   │   └── service/
│   │       └── managed_service.py       # Base class for lifecycle-managed services
│   │
│   ├── decorators/
│   │   └── repo_error_handling.py       # Error handling decorator
│   │
│   ├── logs/
│   │   └── logging_config.py            # Centralized logging config
│   │
│   └── models/                   # Pydantic data models
│       ├── characters.py         # Character validation models
│       ├── enemies.py            # Enemy validation models
│       └── items.py              # (empty - placeholder)
│
├── .env                          # Environment variables (API keys)
├── pyproject.toml               # Poetry dependencies
└── CLAUDE.md                    # This file
```

### Key Design Patterns Implemented

#### 1. **Repository Pattern** (`data_repository.py`)
**Purpose:** Abstracts data access from business logic
**Implementation:**
- `read_data_file()` - Read JSON files
- `write_data_file()` - Write JSON files
- `update_data_file()` - Update specific keys
- `create_data_file()` - Create new files
- Automatic backup system (creates .bak files before writes)
- Path management via PathFinder class

**Why it matters:** MCP tools don't need to know we're using JSON files. Easy to swap to database later.

#### 2. **Decorator Pattern** (`repo_error_handling.py`)
**Purpose:** Centralized error handling without modifying core functions
**Implementation:**
- `@handle_repo_errors` decorator
- Catches: FileNotFoundError, FileExistsError, KeyError, JSONDecodeError
- Logs errors and returns safe defaults (None or {})

**Why it matters:** Don't repeat error handling in every function. Change once, affects everywhere.

#### 3. **Managed Service Pattern** (`managed_service.py`)
**Purpose:** Services with lifecycle management (init, start, stop)
**Implementation:**
- Abstract base class `ManagedService`
- Enum-based ordering for initialization/shutdown
- Service status tracking (INITIALIZING, RUNNING, STOPPING, STOPPED, FAILED)
- Configurable timeouts

**Status:** Infrastructure exists but NO concrete implementations yet. Will be used for DatabaseService, CacheService, etc. when needed.

#### 4. **Path Discovery System** (`path_finder.py`)
**Purpose:** Automatically discover and cache data file paths
**Implementation:**
- Scans data/ directory recursively
- Returns dict: `{"characters": ["setsuna.json"], "campaign": [...], ...}`
- Caching with manual refresh capability

### Data Flow (Planned)
```
Claude → MCP Tool → Service Layer → Repository Layer → JSON Files
         (tools.py)  (not built)   (data_repository)    (data/)
```

**Current Reality:**
```
Claude → MCP Server → ??? (tools.py is empty)
```

---

## User Instruction Log

### Session 1: 2025-12-19 - Initial Mentorship Request

**User Request:**
> "i am a fresh intern. This is my project im building to learn MCP and general industry standard coding. Please read it and evaluate it. I have a mentor which gave me a completed mcp project but its in the works vpn and cant access it now. I want to make my project idustry standard so i can start working by myself. i want you to become my mentor. check my code and suggests what we do next."

**Key Instructions:**
- Act as a mentor, not just a code writer
- Evaluate current code without changing it
- Suggest what to learn BEFORE coding
- Explain concepts from mentor's project (CSM repository, managed services)
- Help understand industry-standard patterns
- **DO NOT change code unless explicitly asked**

**User Context:**
- Fresh intern learning MCP
- Mentor's project has complex patterns (CSM repository, managed services)
- Wants to understand concepts before implementing
- Prefers teaching over doing

**Follow-up Request:**
> "I want to create a persistent memory file for this project so you have context every time I run you."

**Instruction:** Create CLAUDE.md with specific sections for continuity across sessions.

---

## Change Log

### 2025-12-19 - Before Mentorship Session
**Commit:** "Major improvements and changes. Data repository overhauled"
- ✅ DataRepository CRUD operations implemented (99 lines)
- ✅ PathFinder automatic file discovery (38 lines)
- ✅ Error handling decorator (34 lines)
- ✅ Logging configuration (23 lines)
- ✅ ManagedService infrastructure (21 lines)
- ✅ Service lifecycle enums (initialization/shutdown order, status)
- ✅ Pydantic models for Character and Enemy (minimal)
- ⚠️ Tests deleted (72 lines of repo_test.py removed)
- ❌ MCP tools not implemented (tools.py empty)
- ❌ Server is skeleton only (12 lines)

### 2025-12-19 - Mentorship Session Started
- ✅ Created CLAUDE.md for persistent context
- 📝 Conducted comprehensive codebase analysis
- 📝 Identified architecture strengths and gaps
- 📝 Created learning roadmap for intern

---

## Last Output Summary

### Comprehensive Project Evaluation Completed

**Analysis Delivered:**
1. **Full codebase exploration** - Used Task agent to analyze all files, structure, and patterns
2. **Architecture assessment** - Identified Repository Pattern, Decorator Pattern, Managed Service Pattern
3. **Gap analysis** - Found critical missing pieces (MCP tools, tests, security issues)
4. **Concept explanations** - Demystified Repository Pattern, Managed Services, Decorators
5. **Learning roadmap** - Created phased approach: MCP fundamentals → implementation → services → testing

**Key Findings:**
- **Good:** Well-structured, thoughtful patterns, solid repository layer
- **Problem:** Over-engineering before functionality (built foundation without the house)
- **Critical:** No MCP tools implemented (core functionality missing)
- **Security:** .env file not in .gitignore (API key exposed in git)

**Mentoring Approach Established:**
- Teach concepts before implementation
- Start with simplest working solution
- Iterate and refactor only when needed
- Learn by doing, not by over-architecting

**Question Posed to User:**
Asking preferred learning style:
- Option A: Learn by Reading (theory first)
- Option B: Learn by Doing (hands-on immediately)
- Option C: Learn by Exploring (study mentor's code when VPN available)

Awaiting user response to determine next teaching approach.

---

## Next Steps

### 🚨 **Critical Fixes Required (Before Any New Development)**
- [ ] **SECURITY:** Add `.env` to `.gitignore` (API key currently exposed)
- [ ] **SECURITY:** Rotate the exposed Anthropic API key
- [ ] Clean up `src/code dump.py` (example code, not part of project)
- [ ] Decide on learning approach (Reading/Doing/Exploring)

### 📚 **Phase 1: MCP Fundamentals (Learning Phase)**
Learn these concepts before implementing:
- [ ] What is MCP? (Model Context Protocol basics)
- [ ] MCP Architecture (server, tools, resources, prompts)
- [ ] How to register tools with FastMCP
- [ ] Tool arguments and return types
- [ ] Testing MCP tools with Claude Desktop

### 🔧 **Phase 2: First Working MCP Tool (Implementation)**
- [ ] Implement `get_character(name: str)` tool in `tools.py`
- [ ] Connect tool to DataRepository
- [ ] Add Pydantic validation using CharacterModel
- [ ] Test tool with Claude Desktop
- [ ] Verify tool reads `setsuna.json` correctly

### 🚀 **Phase 3: Core MCP Tools Suite**
Once first tool works, expand to full CRUD:
- [ ] `create_character()` - Create new character with validation
- [ ] `update_character()` - Modify character attributes
- [ ] `list_characters()` - Show all available characters
- [ ] `delete_character()` - Remove character (with backup check)
- [ ] Similar tools for enemies: `get_enemy()`, `create_enemy()`, etc.
- [ ] Campaign tools: `get_campaign_state()`, `update_campaign()`

### 🎯 **Phase 4: Data Models Expansion**
- [ ] Add more character classes (Mage, Rogue, Cleric, Ranger)
- [ ] Add more weapons (Bow, Staff, Dagger, Axe)
- [ ] Add more enemy types (Goblin, Dragon, Skeleton, Troll)
- [ ] Implement Items model (potions, armor, loot)
- [ ] Add inventory system to characters

### ✅ **Phase 5: Testing Infrastructure**
- [ ] Restore test structure (was deleted)
- [ ] Write unit tests for DataRepository (CRUD operations)
- [ ] Write unit tests for PathFinder (file discovery)
- [ ] Write integration tests for MCP tools
- [ ] Mock file system for tests (use pytest fixtures)
- [ ] Add test coverage reporting

### 🏗️ **Phase 6: Service Layer (Only If Needed)**
Implement services when complexity justifies them:
- [ ] CharacterService - Business logic for character operations
- [ ] CombatService - Handle battle mechanics
- [ ] InventoryService - Manage items and equipment
- [ ] Connect services to ManagedService lifecycle
- [ ] Implement proper initialization ordering

### 📖 **Phase 7: Documentation & Polish**
- [ ] Write README.md with setup instructions
- [ ] Document each MCP tool (docstrings)
- [ ] Add usage examples
- [ ] Create architecture diagram
- [ ] Write deployment guide

### 🎓 **Learning Milestones**
Track understanding of key concepts:
- [ ] Can explain Repository Pattern and its benefits
- [ ] Can explain when to use Managed Services
- [ ] Understands MCP protocol flow
- [ ] Can write MCP tools independently
- [ ] Can write unit tests
- [ ] Can make architectural tradeoff decisions
- [ ] Understands when NOT to over-engineer

---

## Notes & Reminders

### Important Decisions Pending
1. **Learning approach** - Awaiting user preference (Reading/Doing/Exploring)
2. **Service layer** - Don't implement until actually needed (avoid over-engineering)
3. **Async implementation** - DataRepository has TODO for async, but not needed yet

### Technical Debt
- Multiple TODOs in code (advanced caching, async, model expansion)
- Inconsistent import paths (`from src.` vs `from mcp_training.`)
- PathFinder could be proper singleton (currently just class methods)
- No validation that JSON data matches Pydantic models
- Empty directories (exceptions/, items.py)

### Questions to Address Later
1. Why were tests removed in last commit? (72 lines deleted)
2. What's the vision for ManagedService? (built but unused)
3. Why aiofiles dependency? (not used anywhere yet)
4. What game mechanics are planned? (combat, inventory, quests?)

### Mentor's Project Patterns to Learn (When VPN Available)
- CSM Repository (Campaign State Manager?)
- How managed services are used in practice
- Service layer implementation examples
- Complex file patterns and organization

---

## Success Metrics

### Immediate Goal (This Week)
✅ User understands MCP fundamentals
✅ ONE working MCP tool (`get_character`)
✅ Tool successfully tested with Claude
✅ Security issues resolved

### Short-term Goal (This Month)
✅ Full CRUD operations for characters and enemies
✅ Test suite with >80% coverage
✅ Expanded data models (3+ classes, 5+ weapons)
✅ User can confidently implement new tools independently

### Long-term Goal (Learning Complete)
✅ Production-ready MCP server
✅ User understands when to use which patterns
✅ Can make architectural decisions independently
✅ Comfortable reading and understanding mentor's complex project
✅ Ready to work on real projects independently

---

## Contact & Resources

### Useful Links
- **MCP Documentation:** https://modelcontextprotocol.io/
- **FastMCP Docs:** https://github.com/jlowin/fastmcp
- **Pydantic Docs:** https://docs.pydantic.dev/

### Environment
- **Python Version:** 3.13
- **Package Manager:** Poetry
- **MCP Framework:** FastMCP (mcp 1.23.3)
- **Testing:** pytest
- **Models:** Pydantic 2.12.5

---

**End of Context File**

*This file will be updated after each session to maintain continuity.*
