"""add trgm index

Revision ID: 2e105cb60f58
Revises: 6f318370f938
Create Date: 2024-11-19 12:04:04.547221

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2e105cb60f58"
down_revision = "6f318370f938"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create the pg_trgm extension
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        "event_plate_trgm_idx",
        "event",
        ["plate"],
        unique=False,
        postgresql_ops={"plate": "gin_trgm_ops"},
        postgresql_using="gin",
    )
    op.create_index(
        "record_plate_trgm_idx",
        "record",
        ["plate"],
        unique=False,
        postgresql_ops={"plate": "gin_trgm_ops"},
        postgresql_using="gin",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        "record_plate_trgm_idx",
        table_name="record",
        postgresql_ops={"plate": "gin_trgm_ops"},
        postgresql_using="gin",
    )
    op.drop_index(
        "event_plate_trgm_idx",
        table_name="event",
        postgresql_ops={"plate": "gin_trgm_ops"},
        postgresql_using="gin",
    )
    # ### end Alembic commands ###

    # Create the pg_trgm extension
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")