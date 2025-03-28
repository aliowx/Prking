"""add column id equipment to bill

Revision ID: f133f0ef1fe6
Revises: 0e8cc191ac62
Create Date: 2024-10-16 19:49:50.893114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f133f0ef1fe6'
down_revision = '0e8cc191ac62'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bill', sa.Column('camera_entrance_id', sa.Integer(), nullable=True))
    op.add_column('bill', sa.Column('camera_exit_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_bill_camera_entrance_id'), 'bill', ['camera_entrance_id'], unique=False)
    op.create_index(op.f('ix_bill_camera_exit_id'), 'bill', ['camera_exit_id'], unique=False)
    op.create_foreign_key(None, 'bill', 'equipment', ['camera_entrance_id'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    op.create_foreign_key(None, 'bill', 'equipment', ['camera_exit_id'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bill', type_='foreignkey')
    op.drop_constraint(None, 'bill', type_='foreignkey')
    op.drop_index(op.f('ix_bill_camera_exit_id'), table_name='bill')
    op.drop_index(op.f('ix_bill_camera_entrance_id'), table_name='bill')
    op.drop_column('bill', 'camera_exit_id')
    op.drop_column('bill', 'camera_entrance_id')
    # ### end Alembic commands ###
