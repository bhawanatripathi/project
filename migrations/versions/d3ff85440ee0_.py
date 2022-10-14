"""empty message

Revision ID: d3ff85440ee0
Revises: ba5c2a7a4c48
Create Date: 2022-10-10 12:18:57.640439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3ff85440ee0'
down_revision = 'ba5c2a7a4c48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('acc_type', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'acc_type')
    # ### end Alembic commands ###