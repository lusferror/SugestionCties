"""empty message

Revision ID: 8f71e60633a3
Revises: 2e7679aa003d
Create Date: 2023-01-24 23:57:44.856118

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8f71e60633a3'
down_revision = '2e7679aa003d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ascii', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('feat_code', sa.String(length=20), nullable=True))
        batch_op.drop_column('ascci')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ascci', mysql.VARCHAR(length=20), nullable=True))
        batch_op.drop_column('feat_code')
        batch_op.drop_column('ascii')

    # ### end Alembic commands ###