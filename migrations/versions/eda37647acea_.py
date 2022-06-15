"""empty message

Revision ID: eda37647acea
Revises: 07813235a696
Create Date: 2022-06-15 10:30:06.087516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eda37647acea'
down_revision = '07813235a696'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_link_wiki_links', table_name='link')
    op.create_index(op.f('ix_link_wiki_links'), 'link', ['wiki_links'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_link_wiki_links'), table_name='link')
    op.create_index('ix_link_wiki_links', 'link', ['wiki_links'], unique=False)
    # ### end Alembic commands ###