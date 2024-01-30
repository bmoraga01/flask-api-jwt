"""Second_db

Revision ID: ec70961b54ef
Revises: 
Create Date: 2024-01-30 17:16:44.823708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec70961b54ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ms_discount_type',
    sa.Column('msdt_id', sa.Integer(), nullable=False),
    sa.Column('msdt_desc', sa.String(length=200), nullable=True),
    sa.Column('msdt_active_status', sa.String(length=1), nullable=True),
    sa.PrimaryKeyConstraint('msdt_id')
    )
    op.create_table('ms_discount',
    sa.Column('msd_id', sa.Integer(), nullable=False),
    sa.Column('msd_msdt_id', sa.Integer(), nullable=True),
    sa.Column('msd_desc', sa.String(length=150), nullable=True),
    sa.Column('msd_nominal', sa.NUMERIC(precision=12), nullable=True),
    sa.Column('msd_active_status', sa.String(length=1), nullable=True),
    sa.ForeignKeyConstraint(['msd_msdt_id'], ['ms_discount_type.msdt_id'], ),
    sa.PrimaryKeyConstraint('msd_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ms_discount')
    op.drop_table('ms_discount_type')
    # ### end Alembic commands ###