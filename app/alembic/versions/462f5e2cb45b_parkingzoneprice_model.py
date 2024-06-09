"""parkingzoneprice_model

Revision ID: 462f5e2cb45b
Revises: 79ff4f7d50b0
Create Date: 2024-06-08 17:24:31.123681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '462f5e2cb45b'
down_revision = '79ff4f7d50b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parkingzoneprice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=False),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.Column('price_id', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['price_id'], ['price.id'], ),
    sa.ForeignKeyConstraint(['zone_id'], ['parkingzone.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_parkingzoneprice_created'), 'parkingzoneprice', ['created'], unique=False)
    op.create_index(op.f('ix_parkingzoneprice_id'), 'parkingzoneprice', ['id'], unique=False)
    op.create_index(op.f('ix_parkingzoneprice_is_deleted'), 'parkingzoneprice', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_parkingzoneprice_modified'), 'parkingzoneprice', ['modified'], unique=False)
    op.add_column('price', sa.Column('parking_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'price', 'parking', ['parking_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'price', type_='foreignkey')
    op.drop_column('price', 'parking_id')
    op.drop_index(op.f('ix_parkingzoneprice_modified'), table_name='parkingzoneprice')
    op.drop_index(op.f('ix_parkingzoneprice_is_deleted'), table_name='parkingzoneprice')
    op.drop_index(op.f('ix_parkingzoneprice_id'), table_name='parkingzoneprice')
    op.drop_index(op.f('ix_parkingzoneprice_created'), table_name='parkingzoneprice')
    op.drop_table('parkingzoneprice')
    # ### end Alembic commands ###
