---
trigger: always_on
---

You are an expert in Python, FastAPI, and scalable API development.

Key Principles

- Write clear, structured technical responses with accurate Python examples.
- Use **Class-Based Views and Services** to promote structure and testability.
- **Layered Architecture**: Strictly follow Controller -> Service (Interface -> Impl) -> Repository pattern.
- Use explicit variable names and comprehensive type hints.
- Favor standard "Enterprise" patterns familiar to Spring/Java developers.

Python/FastAPI Architecture

- **Controller**: Handles HTTP requests/responses only. Delegates business logic to Service.
- **Service Layer**:
  - Define an abstract base class (Interface) for services (e.g., `UserService`).
  - Implement the logic in a concrete class (e.g., `UserServiceImpl`).
  - Use Dependency Injection to inject the Service implementation into the Controller.
- **Repository Pattern**: (If DB is used) Isolate data access logic behind a repository interface.
- **DTOs/Schemas**: Use Pydantic models for data transfer (Request/Response bodies).
- **Configuration**: Use a dedicated config service/manager injected into services.

Coding Standards

- Use `def` for synchronous logic and `async def` for I/O bound operations.
- Always use Type Hints.
- **Naming Conventions**:
  - Controllers: `routers/user_controller.py`, `routers/kakao_oauth_controller.py`
  - Services: `services/user_service.py`, `services/user_service_impl.py`
  - Schemas/DTOs: `schemas/user_dto.py` or `schemas/user_schema.py`
- **Error Handling**:
  - Catch exceptions in the Controller and convert them to `HTTPException`.
  - Service layer should raise clean, domain-specific exceptions (e.g., `ValueError`, `UserNotFoundException`).

Structure Example

```
backend/
├── config/
│   └── env.py
├── domain/ (or authentication/)
│   ├── controller/
│   │   └── user_controller.py
│   ├── service/
│   │   ├── user_service.py (Interface)
│   │   └── user_service_impl.py (Implementation)
│   └── schemas/
└── main.py
```

Error Handling and Validation

- Prioritize error handling and edge cases:
  - Handle errors and edge cases at the beginning of functions.
  - Use early returns for error conditions to avoid deeply nested if statements.
  - Place the happy path last in the function for improved readability.
  - Avoid unnecessary else statements; use the if-return pattern instead.
  - Use guard clauses to handle preconditions and invalid states early.
  - Implement proper error logging and user-friendly error messages.
  - Use custom error types or error factories for consistent error handling.

Dependencies

- FastAPI
- Pydantic v2
- Async database libraries like asyncpg or aiomysql
- SQLAlchemy 2.0 (if using ORM features)

FastAPI-Specific Guidelines

- Use functional components (plain functions) and Pydantic models for input validation and response schemas.
- Use declarative route definitions with clear return type annotations.
- Use def for synchronous operations and async def for asynchronous ones.
- Minimize @app.on_event("startup") and @app.on_event("shutdown"); prefer lifespan context managers for managing startup and shutdown events.
- Use middleware for logging, error monitoring, and performance optimization.
- Optimize for performance using async functions for I/O-bound tasks, caching strategies, and lazy loading.
- Use HTTPException for expected errors and model them as specific HTTP responses.
- Use middleware for handling unexpected errors, logging, and error monitoring.
- Use Pydantic's BaseModel for consistent input/output validation and response schemas.

Performance Optimization

- Minimize blocking I/O operations; use asynchronous operations for all database calls and external API requests.
- Implement caching for static and frequently accessed data using tools like Redis or in-memory stores.
- Optimize data serialization and deserialization with Pydantic.
- Use lazy loading techniques for large datasets and substantial API responses.

Key Conventions

1. Rely on FastAPI’s dependency injection system for managing state and shared resources.
2. Prioritize API performance metrics (response time, latency, throughput).
3. Limit blocking operations in routes:
   - Favor asynchronous and non-blocking flows.
   - Use dedicated async functions for database and external API operations.
   - Structure routes and dependencies clearly to optimize readability and maintainability.
