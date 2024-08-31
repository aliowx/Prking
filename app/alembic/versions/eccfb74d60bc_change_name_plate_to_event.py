"""change name plate to event

Revision ID: eccfb74d60bc
Revises: 6b33396f2d5f
Create Date: 2024-08-26 17:55:28.901974

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'eccfb74d60bc'
down_revision = '6b33396f2d5f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plate', sa.String(), nullable=False),
    sa.Column('record_time', sa.DateTime(), nullable=False),
    sa.Column('type_camera', sa.String(), nullable=True),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.Column('spot_id', sa.Integer(), nullable=True),
    sa.Column('camera_id', sa.Integer(), nullable=False),
    sa.Column('record_id', sa.Integer(), nullable=True),
    sa.Column('plate_image_id', sa.Integer(), nullable=True),
    sa.Column('lpr_image_id', sa.Integer(), nullable=True),
    sa.Column('price_model_id', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['camera_id'], ['equipment.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['lpr_image_id'], ['image.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['plate_image_id'], ['image.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['price_model_id'], ['price.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['record_id'], ['record.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['spot_id'], ['spot.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['zone_id'], ['zone.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_camera_id'), 'event', ['camera_id'], unique=False)
    op.create_index(op.f('ix_event_created'), 'event', ['created'], unique=False)
    op.create_index(op.f('ix_event_id'), 'event', ['id'], unique=False)
    op.create_index(op.f('ix_event_is_deleted'), 'event', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_event_lpr_image_id'), 'event', ['lpr_image_id'], unique=False)
    op.create_index(op.f('ix_event_modified'), 'event', ['modified'], unique=False)
    op.create_index(op.f('ix_event_plate'), 'event', ['plate'], unique=False)
    op.create_index(op.f('ix_event_plate_image_id'), 'event', ['plate_image_id'], unique=False)
    op.create_index(op.f('ix_event_price_model_id'), 'event', ['price_model_id'], unique=False)
    op.create_index(op.f('ix_event_record_id'), 'event', ['record_id'], unique=False)
    op.create_index(op.f('ix_event_record_time'), 'event', ['record_time'], unique=False)
    op.create_index(op.f('ix_event_spot_id'), 'event', ['spot_id'], unique=False)
    op.create_index(op.f('ix_event_zone_id'), 'event', ['zone_id'], unique=False)
    op.drop_index('ix_plate_camera_id', table_name='plate')
    op.drop_index('ix_plate_created', table_name='plate')
    op.drop_index('ix_plate_id', table_name='plate')
    op.drop_index('ix_plate_is_deleted', table_name='plate')
    op.drop_index('ix_plate_lpr_image_id', table_name='plate')
    op.drop_index('ix_plate_modified', table_name='plate')
    op.drop_index('ix_plate_plate', table_name='plate')
    op.drop_index('ix_plate_plate_image_id', table_name='plate')
    op.drop_index('ix_plate_price_model_id', table_name='plate')
    op.drop_index('ix_plate_record_id', table_name='plate')
    op.drop_index('ix_plate_record_time', table_name='plate')
    op.drop_index('ix_plate_spot_id', table_name='plate')
    op.drop_index('ix_plate_zone_id', table_name='plate')
    op.drop_table('plate')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plate',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('plate', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('record_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('zone_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('spot_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('camera_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('record_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('plate_image_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lpr_image_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price_model_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_deleted', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('type_camera', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['camera_id'], ['equipment.id'], name='plate_camera_id_fkey', onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['lpr_image_id'], ['image.id'], name='plate_lpr_image_id_fkey', onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['plate_image_id'], ['image.id'], name='plate_plate_image_id_fkey', onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['price_model_id'], ['price.id'], name='plate_price_model_id_fkey', onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['record_id'], ['record.id'], name='plate_record_id_fkey', onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['spot_id'], ['spot.id'], name='plate_spot_id_fkey', onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['zone_id'], ['zone.id'], name='plate_zone_id_fkey', onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='plate_pkey')
    )
    op.create_index('ix_plate_zone_id', 'plate', ['zone_id'], unique=False)
    op.create_index('ix_plate_spot_id', 'plate', ['spot_id'], unique=False)
    op.create_index('ix_plate_record_time', 'plate', ['record_time'], unique=False)
    op.create_index('ix_plate_record_id', 'plate', ['record_id'], unique=False)
    op.create_index('ix_plate_price_model_id', 'plate', ['price_model_id'], unique=False)
    op.create_index('ix_plate_plate_image_id', 'plate', ['plate_image_id'], unique=False)
    op.create_index('ix_plate_plate', 'plate', ['plate'], unique=False)
    op.create_index('ix_plate_modified', 'plate', ['modified'], unique=False)
    op.create_index('ix_plate_lpr_image_id', 'plate', ['lpr_image_id'], unique=False)
    op.create_index('ix_plate_is_deleted', 'plate', ['is_deleted'], unique=False)
    op.create_index('ix_plate_id', 'plate', ['id'], unique=False)
    op.create_index('ix_plate_created', 'plate', ['created'], unique=False)
    op.create_index('ix_plate_camera_id', 'plate', ['camera_id'], unique=False)
    op.drop_index(op.f('ix_event_zone_id'), table_name='event')
    op.drop_index(op.f('ix_event_spot_id'), table_name='event')
    op.drop_index(op.f('ix_event_record_time'), table_name='event')
    op.drop_index(op.f('ix_event_record_id'), table_name='event')
    op.drop_index(op.f('ix_event_price_model_id'), table_name='event')
    op.drop_index(op.f('ix_event_plate_image_id'), table_name='event')
    op.drop_index(op.f('ix_event_plate'), table_name='event')
    op.drop_index(op.f('ix_event_modified'), table_name='event')
    op.drop_index(op.f('ix_event_lpr_image_id'), table_name='event')
    op.drop_index(op.f('ix_event_is_deleted'), table_name='event')
    op.drop_index(op.f('ix_event_id'), table_name='event')
    op.drop_index(op.f('ix_event_created'), table_name='event')
    op.drop_index(op.f('ix_event_camera_id'), table_name='event')
    op.drop_table('event')
    # ### end Alembic commands ###
