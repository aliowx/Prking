"""add column user_id in event

Revision ID: bfcafe7bcb08
Revises: 92b34ded2644
Create Date: 2024-10-06 14:39:13.493429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfcafe7bcb08'
down_revision = '92b34ded2644'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_event_user_id'), 'event', ['user_id'], unique=False)
    op.create_foreign_key(None, 'event', 'user', ['user_id'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_index(op.f('ix_event_user_id'), table_name='event')
    op.drop_column('event', 'user_id')
    # ### end Alembic commands ###
