"""Initial migration

Revision ID: 6890ce5203cb
Revises: b07721b2498f
Create Date: 2022-03-28 22:00:02.142122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6890ce5203cb'
down_revision = 'b07721b2498f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=False),
    sa.Column('account_nr', sa.Integer(), nullable=False),
    sa.Column('vendor_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account_nr')
    )
    op.create_table('work_in_process',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('invoice_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('invoice_nr', sa.String(length=100), nullable=False),
    sa.Column('customer', sa.String(length=100), nullable=False),
    sa.Column('job_name', sa.String(length=500), nullable=False),
    sa.Column('po_nr', sa.String(length=50), nullable=False),
    sa.Column('vendor', sa.String(length=50), nullable=False),
    sa.Column('cogs', sa.Float(precision=20), nullable=False),
    sa.Column('cogs_account', sa.String(length=100), nullable=False),
    sa.Column('invoiced', sa.String(length=5), nullable=False),
    sa.Column('month_invoiced', sa.String(length=50), nullable=True),
    sa.Column('product_at_co', sa.String(length=5), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('invoice_nr'),
    sa.UniqueConstraint('po_nr')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('work_in_process')
    op.drop_table('account')
    # ### end Alembic commands ###
