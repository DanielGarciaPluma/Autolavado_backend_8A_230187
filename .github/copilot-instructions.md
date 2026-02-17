# Copilot Instructions for Autolavado Backend

## Project Overview
FastAPI-based car wash service management backend with a SQLAlchemy ORM layer connected to MySQL. The application manages users, roles, vehicles, and services with a strict layered architecture separating models, schemas, CRUD operations, and routes.

## Architecture & Patterns

### Layered Architecture (CRITICAL Pattern)
The codebase strictly follows a **4-layer architecture**:
1. **Models** (`models/`) - SQLAlchemy ORM classes mapping database tables
2. **Schemas** (`schemas/`) - Pydantic validators for request/response serialization
3. **CRUD** (`crud/`) - Database operations isolated in module-per-entity functions
4. **Routes** (`routes/`) - FastAPI endpoints that orchestrate crud + schema validation

**Example flow**: `routes_rol.py` → `crud_rol.py` → `models/rol.py`, with `schema_rol.py` for validation.

When adding new features, **create files in all 4 layers** - never skip layers or mix concerns.

### Naming Conventions
- **Models**: Singular, PascalCase (e.g., `User`, `Auto`, `Service`)
- **Schemas**: `schema_{entity}.py` with `{Entity}Base`, `{Entity}Create`, `{Entity}Update`, `{Entity}` classes
- **CRUD**: `crud_{entity}.py` with `get_`, `create_`, `update_`, `delete_` functions
- **Routes**: `routes_{entity}.py` using `APIRouter` with prefix matching entity name
- **Tables**: Spanish naming: `tbc_` (catálogos), `tbb_` (base), `tbd_` (detalles)

### Database Configuration
- **Engine**: MySQL at `localhost:3307` (non-standard port)
- **Connection URL**: `mysql://root:1234@localhost:3307/autolavado_db`
- **Session management**: Use `SessionLocal` from `config/db.py` with FastAPI dependency injection
- **Base models**: All models inherit from `Base` in `config/db.py`

### Common Dependencies
- **FastAPI 0.128.0** - Web framework
- **SQLAlchemy** with MySQL driver - ORM
- **Pydantic v2** - Data validation
- **python-dotenv** - Environment variables (set up for credentials)

## CRUD Operation Patterns

All CRUD functions follow this pattern:
```python
def get_entities(db: Session, skip: int = 0, limit: int = 100):
    '''Function description in Spanish'''
    return db.query(EntityModel).offset(skip).limit(limit).all()
```

**Standard operations to implement**:
- `get_{entity}()` - List with pagination (skip/limit)
- `create_{entity}()` - Create with schema validation
- `update_{entity}()` - Update existing record
- `delete_{entity}()` - Soft/hard delete

Always receive `db: Session` as first parameter for dependency injection from routes.

## Authentication & Security Notes
- **Password field**: Stored as plaintext in `contrasena` column (NOT production-ready)
- **Login schema**: `UserLogin` supports both phone and email with optional fields
- **Future work**: Implement password hashing (bcrypt) and JWT tokens before production

## Timestamp Management
Models use `datetime` fields:
- `fecha_registro` - Created timestamp (set at creation)
- `fecha_actualizacion` / `fecha_modificacion` - Update timestamp (auto-update on changes)

Import `from datetime import datetime` when creating records in CRUD functions.

## Common Pitfalls
- ❌ Mixing business logic into route handlers instead of CRUD layer
- ❌ Creating models without corresponding schema classes
- ❌ Missing `__tablename__` in model definitions
- ❌ Inconsistent use of `Session` dependency in routes
- ❌ Spanish comments required for documentation (project standard)

## Development Workflow

### Running the Server
```bash
uvicorn main.py:app --reload  # Development with auto-reload
```
Main entry point is `main.py` - currently contains placeholder endpoints.

### Testing Database Connection
The connection string in `config/db.py` points to localhost:3307. Verify MySQL is running on this non-standard port before development.

## Adding New Features Checklist
1. Create SQLAlchemy model in `models/{entity}.py`
2. Create Pydantic schemas in `schemas/schema_{entity}.py` (3 classes: Base/Create/Update)
3. Implement CRUD functions in `crud/crud_{entity}.py`
4. Create routes in `routes/routes_{entity}.py` using APIRouter
5. Import route in `main.py` and include router with appropriate prefix
6. Include Spanish docstrings for all functions and classes

---

## Key Files to Reference
- [config/db.py](config/db.py) - Database setup and session management
- [models/user.py](models/user.py) - Complete model example with relationships
- [schemas/schema_user.py](schemas/schema_user.py) - Complete schema pattern (3 classes)
- [crud/crud_rol.py](crud/crud_rol.py) - CRUD operation examples
- [routes/routes_rol.py](routes/routes_rol.py) - Route endpoint patterns
