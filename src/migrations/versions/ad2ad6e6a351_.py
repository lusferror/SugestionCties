"""empty message

Revision ID: ad2ad6e6a351
Revises: 8f71e60633a3
Create Date: 2023-01-25 00:25:31.238163

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ad2ad6e6a351'
down_revision = '8f71e60633a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.alter_column('alt_name',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.alter_column('alt_name',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=True)

    # ### end Alembic commands ###
