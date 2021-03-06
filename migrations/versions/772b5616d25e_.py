"""empty message

Revision ID: 772b5616d25e
Revises: ced7dfe5a1fc
Create Date: 2021-05-01 18:26:30.965909

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '772b5616d25e'
down_revision = 'ced7dfe5a1fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=True)
    # ### end Alembic commands ###
