from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
order = Table('order', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=140)),
    Column('product', String(length=20)),
    Column('options', String(length=140)),
    Column('order_date', DateTime),
    Column('order_type', String(length=20)),
    Column('paid', Boolean),
    Column('paid_date', DateTime),
    Column('shipped', Boolean),
    Column('shipped_date', DateTime),
    Column('tracking', String(length=80)),
    Column('address1', String(length=80)),
    Column('address2', String(length=80)),
    Column('city', String(length=80)),
    Column('state', String(length=80)),
    Column('postalCode', String(length=80)),
    Column('country', String(length=80)),
    Column('comments', String(length=500)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['order'].columns['address1'].create()
    post_meta.tables['order'].columns['address2'].create()
    post_meta.tables['order'].columns['city'].create()
    post_meta.tables['order'].columns['country'].create()
    post_meta.tables['order'].columns['postalCode'].create()
    post_meta.tables['order'].columns['state'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['order'].columns['address1'].drop()
    post_meta.tables['order'].columns['address2'].drop()
    post_meta.tables['order'].columns['city'].drop()
    post_meta.tables['order'].columns['country'].drop()
    post_meta.tables['order'].columns['postalCode'].drop()
    post_meta.tables['order'].columns['state'].drop()
