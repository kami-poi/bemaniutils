"""Get rid of plays column, use count of columns in score_history instead.

Revision ID: 437a91b37583
Revises: 3e1cda9a853f
Create Date: 2017-01-17 23:17:42.514334

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '437a91b37583'
down_revision = '3e1cda9a853f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('score', 'plays')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score', sa.Column('plays', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
