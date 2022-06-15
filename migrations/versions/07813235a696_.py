"""empty message

Revision ID: 07813235a696
Revises: 5b049bfa767b
Create Date: 2022-06-15 10:29:07.475970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07813235a696'
down_revision = '5b049bfa767b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_link_wiki_topic', table_name='link')
    op.create_index(op.f('ix_link_wiki_topic'), 'link', ['wiki_topic'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_link_wiki_topic'), table_name='link')
    op.create_index('ix_link_wiki_topic', 'link', ['wiki_topic'], unique=False)
    # ### end Alembic commands ###