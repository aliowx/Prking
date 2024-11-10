"""refactor

Revision ID: 7e4a3a5cdcfa
Revises: 
Create Date: 2024-07-03 17:27:28.114130

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7e4a3a5cdcfa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_image_created'), 'image', ['created'], unique=False)
    op.create_index(op.f('ix_image_id'), 'image', ['id'], unique=False)
    op.create_index(op.f('ix_image_is_deleted'), 'image', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_image_modified'), 'image', ['modified'], unique=False)
    op.create_table('parking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('brand_name', sa.String(length=50), nullable=True),
    sa.Column('floor_count', sa.Integer(), nullable=True),
    sa.Column('area', sa.Integer(), nullable=True),
    sa.Column('location_lat', sa.NUMERIC(precision=10, scale=7), nullable=True),
    sa.Column('location_lon', sa.NUMERIC(precision=10, scale=7), nullable=True),
    sa.Column('parking_address', sa.String(), nullable=True),
    sa.Column('parking_logo_base64', sa.String(), nullable=True),
    sa.Column('owner_first_name', sa.String(length=50), nullable=True),
    sa.Column('owner_last_name', sa.String(length=50), nullable=True),
    sa.Column('owner_national_id', sa.String(length=50), nullable=True),
    sa.Column('owner_postal_code', sa.String(length=50), nullable=True),
    sa.Column('owner_phone_number', sa.String(length=50), nullable=True),
    sa.Column('owner_email', sa.String(length=50), nullable=True),
    sa.Column('owner_sheba_number', sa.String(length=50), nullable=True),
    sa.Column('owner_address', sa.String(), nullable=True),
    sa.Column('owner_type', sa.Integer(), nullable=True),
    sa.Column('payment_type', sa.Integer(), nullable=True),
    sa.Column('beneficiary_data', sa.JSON(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_parking_created'), 'parking', ['created'], unique=False)
    op.create_index(op.f('ix_parking_id'), 'parking', ['id'], unique=False)
    op.create_index(op.f('ix_parking_is_deleted'), 'parking', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_parking_modified'), 'parking', ['modified'], unique=False)
    op.create_table('price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('name_fa', sa.String(length=50), nullable=True),
    sa.Column('weekly_days', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('entrance_fee', sa.BigInteger(), nullable=True),
    sa.Column('hourly_fee', sa.BigInteger(), nullable=True),
    sa.Column('daily_fee', sa.BigInteger(), nullable=True),
    sa.Column('penalty_fee', sa.BigInteger(), nullable=True),
    sa.Column('expiration_datetime', sa.DateTime(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_price_created'), 'price', ['created'], unique=False)
    op.create_index(op.f('ix_price_expiration_datetime'), 'price', ['expiration_datetime'], unique=False)
    op.create_index(op.f('ix_price_id'), 'price', ['id'], unique=False)
    op.create_index(op.f('ix_price_is_deleted'), 'price', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_price_modified'), 'price', ['modified'], unique=False)
    op.create_table('rule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_fa', sa.String(length=50), nullable=False),
    sa.Column('rule_type', sa.Integer(), nullable=True),
    sa.Column('weekdays', postgresql.ARRAY(sa.Integer()), nullable=False),
    sa.Column('start_datetime', sa.DateTime(), nullable=True),
    sa.Column('end_datetime', sa.DateTime(), nullable=True),
    sa.Column('registeration_date', sa.Date(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rule_created'), 'rule', ['created'], unique=False)
    op.create_index(op.f('ix_rule_id'), 'rule', ['id'], unique=False)
    op.create_index(op.f('ix_rule_is_deleted'), 'rule', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_rule_modified'), 'rule', ['modified'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_created'), 'user', ['created'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_is_deleted'), 'user', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_user_modified'), 'user', ['modified'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    op.create_table('zone',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('tag', sa.String(length=50), nullable=True),
    sa.Column('floor_number', sa.Integer(), nullable=True),
    sa.Column('floor_name', sa.String(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['zone.id'], initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['zone.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_zone_created'), 'zone', ['created'], unique=False)
    op.create_index(op.f('ix_zone_id'), 'zone', ['id'], unique=False)
    op.create_index(op.f('ix_zone_is_deleted'), 'zone', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_zone_modified'), 'zone', ['modified'], unique=False)
    op.create_table('equipment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('equipment_type', sa.Integer(), nullable=True),
    sa.Column('equipment_status', sa.Integer(), nullable=True),
    sa.Column('serial_number', sa.String(length=50), nullable=True),
    sa.Column('ip_address', sa.String(length=15), nullable=True),
    sa.Column('additional_data', sa.JSON(), nullable=False),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['image.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['zone_id'], ['zone.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_equipment_created'), 'equipment', ['created'], unique=False)
    op.create_index(op.f('ix_equipment_id'), 'equipment', ['id'], unique=False)
    op.create_index(op.f('ix_equipment_image_id'), 'equipment', ['image_id'], unique=False)
    op.create_index(op.f('ix_equipment_is_deleted'), 'equipment', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_equipment_modified'), 'equipment', ['modified'], unique=False)
    op.create_table('platerule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plate', sa.String(length=50), nullable=False),
    sa.Column('rule_id', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['rule_id'], ['rule.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_platerule_created'), 'platerule', ['created'], unique=False)
    op.create_index(op.f('ix_platerule_id'), 'platerule', ['id'], unique=False)
    op.create_index(op.f('ix_platerule_is_deleted'), 'platerule', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_platerule_modified'), 'platerule', ['modified'], unique=False)
    op.create_table('zoneprice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=False),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.Column('price_id', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['price_id'], ['price.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['zone_id'], ['zone.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_zoneprice_created'), 'zoneprice', ['created'], unique=False)
    op.create_index(op.f('ix_zoneprice_id'), 'zoneprice', ['id'], unique=False)
    op.create_index(op.f('ix_zoneprice_is_deleted'), 'zoneprice', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_zoneprice_modified'), 'zoneprice', ['modified'], unique=False)
    op.create_table('zonerule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.Column('rule_id', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['rule_id'], ['rule.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['zone_id'], ['zone.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_zonerule_created'), 'zonerule', ['created'], unique=False)
    op.create_index(op.f('ix_zonerule_id'), 'zonerule', ['id'], unique=False)
    op.create_index(op.f('ix_zonerule_is_deleted'), 'zonerule', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_zonerule_modified'), 'zonerule', ['modified'], unique=False)
    op.create_table('spot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_spot', sa.String(), nullable=True),
    sa.Column('percent_rotation_rectangle_small', sa.Integer(), nullable=True),
    sa.Column('percent_rotation_rectangle_big', sa.Integer(), nullable=True),
    sa.Column('coordinates_rectangle_big', sa.ARRAY(sa.Float()), nullable=True),
    sa.Column('coordinates_rectangle_small', sa.ARRAY(sa.Float()), nullable=True),
    sa.Column('number_line', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('plate', sa.String(), nullable=True),
    sa.Column('latest_time_modified', sa.DateTime(timezone=True), nullable=False),
    sa.Column('camera_id', sa.Integer(), nullable=True),
    sa.Column('plate_image_id', sa.Integer(), nullable=True),
    sa.Column('lpr_image_id', sa.Integer(), nullable=True),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['camera_id'], ['equipment.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['lpr_image_id'], ['image.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['plate_image_id'], ['image.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['zone_id'], ['zone.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_spot_camera_id'), 'spot', ['camera_id'], unique=False)
    op.create_index(op.f('ix_spot_coordinates_rectangle_big'), 'spot', ['coordinates_rectangle_big'], unique=False)
    op.create_index(op.f('ix_spot_coordinates_rectangle_small'), 'spot', ['coordinates_rectangle_small'], unique=False)
    op.create_index(op.f('ix_spot_created'), 'spot', ['created'], unique=False)
    op.create_index(op.f('ix_spot_id'), 'spot', ['id'], unique=False)
    op.create_index(op.f('ix_spot_is_deleted'), 'spot', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_spot_latest_time_modified'), 'spot', ['latest_time_modified'], unique=False)
    op.create_index(op.f('ix_spot_lpr_image_id'), 'spot', ['lpr_image_id'], unique=False)
    op.create_index(op.f('ix_spot_modified'), 'spot', ['modified'], unique=False)
    op.create_index(op.f('ix_spot_plate_image_id'), 'spot', ['plate_image_id'], unique=False)
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plate', sa.String(), nullable=True),
    sa.Column('start_time', sa.DateTime(timezone=True), nullable=False),
    sa.Column('end_time', sa.DateTime(timezone=True), nullable=False),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('best_lpr_image_id', sa.Integer(), nullable=True),
    sa.Column('best_plate_image_id', sa.Integer(), nullable=True),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.Column('spot_id', sa.Integer(), nullable=True),
    sa.Column('price_model_id', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['best_lpr_image_id'], ['image.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['best_plate_image_id'], ['image.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['price_model_id'], ['price.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['spot_id'], ['spot.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['zone_id'], ['zone.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_record_best_lpr_image_id'), 'record', ['best_lpr_image_id'], unique=False)
    op.create_index(op.f('ix_record_best_plate_image_id'), 'record', ['best_plate_image_id'], unique=False)
    op.create_index(op.f('ix_record_created'), 'record', ['created'], unique=False)
    op.create_index(op.f('ix_record_end_time'), 'record', ['end_time'], unique=False)
    op.create_index(op.f('ix_record_id'), 'record', ['id'], unique=False)
    op.create_index(op.f('ix_record_is_deleted'), 'record', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_record_modified'), 'record', ['modified'], unique=False)
    op.create_index(op.f('ix_record_plate'), 'record', ['plate'], unique=False)
    op.create_index(op.f('ix_record_price_model_id'), 'record', ['price_model_id'], unique=False)
    op.create_index(op.f('ix_record_score'), 'record', ['score'], unique=False)
    op.create_index(op.f('ix_record_spot_id'), 'record', ['spot_id'], unique=False)
    op.create_index(op.f('ix_record_start_time'), 'record', ['start_time'], unique=False)
    op.create_index(op.f('ix_record_zone_id'), 'record', ['zone_id'], unique=False)
    op.create_table('plate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plate', sa.String(), nullable=False),
    sa.Column('record_time', sa.DateTime(timezone=True), nullable=False),
    sa.Column('type_status_spot', sa.String(), nullable=True),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.Column('spot_id', sa.Integer(), nullable=True),
    sa.Column('camera_id', sa.Integer(), nullable=False),
    sa.Column('record_id', sa.Integer(), nullable=True),
    sa.Column('plate_image_id', sa.Integer(), nullable=True),
    sa.Column('lpr_image_id', sa.Integer(), nullable=True),
    sa.Column('price_model_id', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['camera_id'], ['equipment.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['lpr_image_id'], ['image.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['plate_image_id'], ['image.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['price_model_id'], ['price.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['record_id'], ['record.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['spot_id'], ['spot.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['zone_id'], ['zone.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_plate_camera_id'), 'plate', ['camera_id'], unique=False)
    op.create_index(op.f('ix_plate_created'), 'plate', ['created'], unique=False)
    op.create_index(op.f('ix_plate_id'), 'plate', ['id'], unique=False)
    op.create_index(op.f('ix_plate_is_deleted'), 'plate', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_plate_lpr_image_id'), 'plate', ['lpr_image_id'], unique=False)
    op.create_index(op.f('ix_plate_modified'), 'plate', ['modified'], unique=False)
    op.create_index(op.f('ix_plate_plate'), 'plate', ['plate'], unique=False)
    op.create_index(op.f('ix_plate_plate_image_id'), 'plate', ['plate_image_id'], unique=False)
    op.create_index(op.f('ix_plate_price_model_id'), 'plate', ['price_model_id'], unique=False)
    op.create_index(op.f('ix_plate_record_id'), 'plate', ['record_id'], unique=False)
    op.create_index(op.f('ix_plate_record_time'), 'plate', ['record_time'], unique=False)
    op.create_index(op.f('ix_plate_spot_id'), 'plate', ['spot_id'], unique=False)
    op.create_index(op.f('ix_plate_zone_id'), 'plate', ['zone_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_plate_zone_id'), table_name='plate')
    op.drop_index(op.f('ix_plate_spot_id'), table_name='plate')
    op.drop_index(op.f('ix_plate_record_time'), table_name='plate')
    op.drop_index(op.f('ix_plate_record_id'), table_name='plate')
    op.drop_index(op.f('ix_plate_price_model_id'), table_name='plate')
    op.drop_index(op.f('ix_plate_plate_image_id'), table_name='plate')
    op.drop_index(op.f('ix_plate_plate'), table_name='plate')
    op.drop_index(op.f('ix_plate_modified'), table_name='plate')
    op.drop_index(op.f('ix_plate_lpr_image_id'), table_name='plate')
    op.drop_index(op.f('ix_plate_is_deleted'), table_name='plate')
    op.drop_index(op.f('ix_plate_id'), table_name='plate')
    op.drop_index(op.f('ix_plate_created'), table_name='plate')
    op.drop_index(op.f('ix_plate_camera_id'), table_name='plate')
    op.drop_table('plate')
    op.drop_index(op.f('ix_record_zone_id'), table_name='record')
    op.drop_index(op.f('ix_record_start_time'), table_name='record')
    op.drop_index(op.f('ix_record_spot_id'), table_name='record')
    op.drop_index(op.f('ix_record_score'), table_name='record')
    op.drop_index(op.f('ix_record_price_model_id'), table_name='record')
    op.drop_index(op.f('ix_record_plate'), table_name='record')
    op.drop_index(op.f('ix_record_modified'), table_name='record')
    op.drop_index(op.f('ix_record_is_deleted'), table_name='record')
    op.drop_index(op.f('ix_record_id'), table_name='record')
    op.drop_index(op.f('ix_record_end_time'), table_name='record')
    op.drop_index(op.f('ix_record_created'), table_name='record')
    op.drop_index(op.f('ix_record_best_plate_image_id'), table_name='record')
    op.drop_index(op.f('ix_record_best_lpr_image_id'), table_name='record')
    op.drop_table('record')
    op.drop_index(op.f('ix_spot_plate_image_id'), table_name='spot')
    op.drop_index(op.f('ix_spot_modified'), table_name='spot')
    op.drop_index(op.f('ix_spot_lpr_image_id'), table_name='spot')
    op.drop_index(op.f('ix_spot_latest_time_modified'), table_name='spot')
    op.drop_index(op.f('ix_spot_is_deleted'), table_name='spot')
    op.drop_index(op.f('ix_spot_id'), table_name='spot')
    op.drop_index(op.f('ix_spot_created'), table_name='spot')
    op.drop_index(op.f('ix_spot_coordinates_rectangle_small'), table_name='spot')
    op.drop_index(op.f('ix_spot_coordinates_rectangle_big'), table_name='spot')
    op.drop_index(op.f('ix_spot_camera_id'), table_name='spot')
    op.drop_table('spot')
    op.drop_index(op.f('ix_zonerule_modified'), table_name='zonerule')
    op.drop_index(op.f('ix_zonerule_is_deleted'), table_name='zonerule')
    op.drop_index(op.f('ix_zonerule_id'), table_name='zonerule')
    op.drop_index(op.f('ix_zonerule_created'), table_name='zonerule')
    op.drop_table('zonerule')
    op.drop_index(op.f('ix_zoneprice_modified'), table_name='zoneprice')
    op.drop_index(op.f('ix_zoneprice_is_deleted'), table_name='zoneprice')
    op.drop_index(op.f('ix_zoneprice_id'), table_name='zoneprice')
    op.drop_index(op.f('ix_zoneprice_created'), table_name='zoneprice')
    op.drop_table('zoneprice')
    op.drop_index(op.f('ix_platerule_modified'), table_name='platerule')
    op.drop_index(op.f('ix_platerule_is_deleted'), table_name='platerule')
    op.drop_index(op.f('ix_platerule_id'), table_name='platerule')
    op.drop_index(op.f('ix_platerule_created'), table_name='platerule')
    op.drop_table('platerule')
    op.drop_index(op.f('ix_equipment_modified'), table_name='equipment')
    op.drop_index(op.f('ix_equipment_is_deleted'), table_name='equipment')
    op.drop_index(op.f('ix_equipment_image_id'), table_name='equipment')
    op.drop_index(op.f('ix_equipment_id'), table_name='equipment')
    op.drop_index(op.f('ix_equipment_created'), table_name='equipment')
    op.drop_table('equipment')
    op.drop_index(op.f('ix_zone_modified'), table_name='zone')
    op.drop_index(op.f('ix_zone_is_deleted'), table_name='zone')
    op.drop_index(op.f('ix_zone_id'), table_name='zone')
    op.drop_index(op.f('ix_zone_created'), table_name='zone')
    op.drop_table('zone')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_modified'), table_name='user')
    op.drop_index(op.f('ix_user_is_deleted'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_created'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_rule_modified'), table_name='rule')
    op.drop_index(op.f('ix_rule_is_deleted'), table_name='rule')
    op.drop_index(op.f('ix_rule_id'), table_name='rule')
    op.drop_index(op.f('ix_rule_created'), table_name='rule')
    op.drop_table('rule')
    op.drop_index(op.f('ix_price_modified'), table_name='price')
    op.drop_index(op.f('ix_price_is_deleted'), table_name='price')
    op.drop_index(op.f('ix_price_id'), table_name='price')
    op.drop_index(op.f('ix_price_expiration_datetime'), table_name='price')
    op.drop_index(op.f('ix_price_created'), table_name='price')
    op.drop_table('price')
    op.drop_index(op.f('ix_parking_modified'), table_name='parking')
    op.drop_index(op.f('ix_parking_is_deleted'), table_name='parking')
    op.drop_index(op.f('ix_parking_id'), table_name='parking')
    op.drop_index(op.f('ix_parking_created'), table_name='parking')
    op.drop_table('parking')
    op.drop_index(op.f('ix_image_modified'), table_name='image')
    op.drop_index(op.f('ix_image_is_deleted'), table_name='image')
    op.drop_index(op.f('ix_image_id'), table_name='image')
    op.drop_index(op.f('ix_image_created'), table_name='image')
    op.drop_table('image')
    # ### end Alembic commands ###