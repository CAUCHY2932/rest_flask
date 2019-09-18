"""empty message

Revision ID: 9c32152b0e72
Revises: 
Create Date: 2019-09-17 16:47:55.523396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c32152b0e72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('standard_person',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('perne', sa.String(length=16), nullable=True),
    sa.Column('begda', sa.Date(), nullable=True),
    sa.Column('endda', sa.Date(), nullable=True),
    sa.Column('massn', sa.String(length=16), nullable=True),
    sa.Column('zczlx', sa.String(length=50), nullable=True),
    sa.Column('massg', sa.String(length=16), nullable=True),
    sa.Column('zczyy', sa.String(length=50), nullable=True),
    sa.Column('stat1', sa.String(length=16), nullable=True),
    sa.Column('zkhtd', sa.String(length=50), nullable=True),
    sa.Column('stat2', sa.String(length=16), nullable=True),
    sa.Column('zgyzt', sa.String(length=50), nullable=True),
    sa.Column('aedat', sa.String(length=20), nullable=True),
    sa.Column('zflag', sa.String(length=50), nullable=True),
    sa.Column('insert_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('addr', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('standard_person')
    op.drop_table('article')
    # ### end Alembic commands ###
