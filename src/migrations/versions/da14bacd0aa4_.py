"""empty message

Revision ID: da14bacd0aa4
Revises: 323eb977a623
Create Date: 2023-01-25 00:39:30.854022

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'da14bacd0aa4'
down_revision = '323eb977a623'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.alter_column('alt_name',
               existing_type=mysql.VARCHAR(length=300),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.alter_column('alt_name',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=300),
               existing_nullable=True)

    # ### end Alembic commands ###