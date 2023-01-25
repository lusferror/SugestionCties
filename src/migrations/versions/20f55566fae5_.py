"""empty message

Revision ID: 20f55566fae5
Revises: 
Create Date: 2023-01-24 23:30:45.115726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20f55566fae5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('ascci', sa.String(length=20), nullable=True),
    sa.Column('alt_name', sa.String(length=20), nullable=True),
    sa.Column('lat', sa.String(length=20), nullable=True),
    sa.Column('long', sa.String(length=20), nullable=True),
    sa.Column('feat_class', sa.String(length=20), nullable=True),
    sa.Column('country', sa.String(length=20), nullable=True),
    sa.Column('cc2', sa.String(length=20), nullable=True),
    sa.Column('admin1', sa.String(length=20), nullable=True),
    sa.Column('admin2', sa.String(length=20), nullable=True),
    sa.Column('admin3', sa.String(length=20), nullable=True),
    sa.Column('admin4', sa.String(length=20), nullable=True),
    sa.Column('population', sa.String(length=20), nullable=True),
    sa.Column('elevation', sa.String(length=20), nullable=True),
    sa.Column('dem', sa.String(length=20), nullable=True),
    sa.Column('tz', sa.String(length=20), nullable=True),
    sa.Column('modified_at', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    # ### end Alembic commands ###