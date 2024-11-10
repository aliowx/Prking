"""add column camera_entrance camera_exit to record

Revision ID: 92b34ded2644
Revises: a50c89cf5aca
Create Date: 2024-10-05 17:11:33.956069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92b34ded2644'
down_revision = 'a50c89cf5aca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('record', sa.Column('camera_entrance_id', sa.Integer(), nullable=True))
    op.add_column('record', sa.Column('camera_exit_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_record_camera_entrance_id'), 'record', ['camera_entrance_id'], unique=False)
    op.create_index(op.f('ix_record_camera_exit_id'), 'record', ['camera_exit_id'], unique=False)
    op.create_foreign_key(None, 'record', 'equipment', ['camera_exit_id'], ['id'])
    op.create_foreign_key(None, 'record', 'equipment', ['camera_entrance_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'record', type_='foreignkey')
    op.drop_constraint(None, 'record', type_='foreignkey')
    op.drop_index(op.f('ix_record_camera_exit_id'), table_name='record')
    op.drop_index(op.f('ix_record_camera_entrance_id'), table_name='record')
    op.drop_column('record', 'camera_exit_id')
    op.drop_column('record', 'camera_entrance_id')
    # ### end Alembic commands ###