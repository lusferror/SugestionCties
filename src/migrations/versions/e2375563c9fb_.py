"""empty message

Revision ID: e2375563c9fb
Revises: ad2ad6e6a351
Create Date: 2023-01-25 00:30:34.612090

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e2375563c9fb'
down_revision = 'ad2ad6e6a351'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.alter_column('alt_name',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=300),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.alter_column('alt_name',
               existing_type=sa.String(length=300),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###