"""add column vehicle color and model into model plate

Revision ID: 34d622869c71
Revises: b5c232512d2a
Create Date: 2024-11-03 11:35:55.008298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34d622869c71'
down_revision = 'b5c232512d2a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('platelist', sa.Column('vehicle_model', sa.String(), nullable=True))
    op.add_column('platelist', sa.Column('vehicle_color', sa.String(), nullable=True))
    op.drop_index('ix_platelist_plate', table_name='platelist')
    op.create_index(op.f('ix_platelist_plate'), 'platelist', ['plate'], unique=False)
    op.create_index(op.f('ix_platelist_vehicle_color'), 'platelist', ['vehicle_color'], unique=False)
    op.create_index(op.f('ix_platelist_vehicle_model'), 'platelist', ['vehicle_model'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_platelist_vehicle_model'), table_name='platelist')
    op.drop_index(op.f('ix_platelist_vehicle_color'), table_name='platelist')
    op.drop_index(op.f('ix_platelist_plate'), table_name='platelist')
    op.create_index('ix_platelist_plate', 'platelist', ['plate'], unique=True)
    op.drop_column('platelist', 'vehicle_color')
    op.drop_column('platelist', 'vehicle_model')
    # ### end Alembic commands ###
