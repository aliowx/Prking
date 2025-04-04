"""delete column expire start and end into plate

Revision ID: 2fd483278b5a
Revises: 34d622869c71
Create Date: 2024-11-03 11:58:27.542542

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2fd483278b5a'
down_revision = '34d622869c71'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_platelist_expire_end', table_name='platelist')
    op.drop_index('ix_platelist_expire_start', table_name='platelist')
    op.drop_column('platelist', 'expire_start')
    op.drop_column('platelist', 'expire_end')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('platelist', sa.Column('expire_end', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('platelist', sa.Column('expire_start', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.create_index('ix_platelist_expire_start', 'platelist', ['expire_start'], unique=False)
    op.create_index('ix_platelist_expire_end', 'platelist', ['expire_end'], unique=False)
    # ### end Alembic commands ###
