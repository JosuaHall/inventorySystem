"""Initial migration

Revision ID: 9f3b62ea7df8
Revises: a99552f8c345
Create Date: 2022-04-13 11:20:14.466838

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9f3b62ea7df8'
down_revision = 'a99552f8c345'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('work_in_process', sa.Column('exception', sa.String(length=50), nullable=True))
    op.alter_column('work_in_process', 'invoiced',
               existing_type=mysql.VARCHAR(length=5),
               nullable=True)
    op.alter_column('work_in_process', 'product_at_co',
               existing_type=mysql.VARCHAR(length=5),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('work_in_process', 'product_at_co',
               existing_type=mysql.VARCHAR(length=5),
               nullable=False)
    op.alter_column('work_in_process', 'invoiced',
               existing_type=mysql.VARCHAR(length=5),
               nullable=False)
    op.drop_column('work_in_process', 'exception')
    # ### end Alembic commands ###