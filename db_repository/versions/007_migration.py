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
    Column('paid', Boolean),
    Column('paid_date', DateTime),
    Column('shipped', Boolean),
    Column('shipped_date', DateTime),
    Column('tracking', String(length=80)),
    Column('comments', String(length=500)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['order'].columns['comments'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['order'].columns['comments'].drop()
