"""empty message

Revision ID: 8bec5a3ee7c1
Revises: fbdd2ba47e65
Create Date: 2021-04-24 18:55:42.662588

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8bec5a3ee7c1'
down_revision = 'fbdd2ba47e65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artists_shows')
    op.drop_column('Artist', 'past_shows')
    op.drop_column('Artist', 'upcoming_shows')
    op.add_column('Show', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'])
    op.drop_column('Show', 'venue_name')
    op.drop_column('Show', 'venue_image_link')
    op.drop_column('Venue', 'past_shows')
    op.drop_column('Venue', 'upcoming_shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('upcoming_shows', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('past_shows', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.add_column('Show', sa.Column('venue_image_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('Show', sa.Column('venue_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_column('Show', 'artist_id')
    op.add_column('Artist', sa.Column('upcoming_shows', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('past_shows', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.create_table('artists_shows',
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('show_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], name='artists_shows_artist_id_fkey'),
    sa.ForeignKeyConstraint(['show_id'], ['Show.id'], name='artists_shows_show_id_fkey'),
    sa.PrimaryKeyConstraint('artist_id', 'show_id', name='artists_shows_pkey')
    )
    # ### end Alembic commands ###
