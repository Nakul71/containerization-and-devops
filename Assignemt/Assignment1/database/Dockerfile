# ─── Stage 1: Builder ──────────────────────────────────────────
FROM postgres:16-alpine AS builder

# Copy custom initialization scripts
COPY init.sql /docker-entrypoint-initdb.d/


# ─── Stage 2: Runtime ─────────────────────────────────────────
FROM postgres:16-alpine AS runtime

LABEL maintainer="nakul" \
      description="Custom PostgreSQL Database for Student Management API"

# Copy init scripts from builder
COPY --from=builder /docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/

# Set default environment variables
ENV POSTGRES_DB=appdb \
    POSTGRES_USER=appuser \
    POSTGRES_PASSWORD=apppassword

# PostgreSQL data directory
VOLUME ["/var/lib/postgresql/data"]

EXPOSE 5432

HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=5 \
    CMD pg_isready -U $POSTGRES_USER -d $POSTGRES_DB || exit 1
