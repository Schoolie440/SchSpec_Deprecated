from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
smart_switch_order = Table('smart_switch_order', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=140)),
    Column('order_date', DateTime),
    Column('paid', Boolean),
    Column('paid_date', DateTime),
    Column('shipped', Boolean),
    Column('shipped_date', DateTime),
    Column('tracking', String(length=80)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['smart_switch_order'].columns['paid'].create()
    post_meta.tables['smart_switch_order'].columns['paid_date'].create()
    post_meta.tables['smart_switch_order'].columns['shipped'].create()
    post_meta.tables['smart_switch_order'].columns['shipped_date'].create()
    post_meta.tables['smart_switch_order'].columns['tracking'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['smart_switch_order'].columns['paid'].drop()
    post_meta.tables['smart_switch_order'].columns['paid_date'].drop()
    post_meta.tables['smart_switch_order'].columns['shipped'].drop()
    post_meta.tables['smart_switch_order'].columns['shipped_date'].drop()
    post_meta.tables['smart_switch_order'].columns['tracking'].drop()
