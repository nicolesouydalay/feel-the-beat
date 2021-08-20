"""empty message
Revision ID: dbf01303e0ab
Revises: d4d72c91968f
Create Date: 2021-08-17 10:58:31.142035
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbf01303e0ab'
down_revision = 'd4d72c91968f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('refresh_token', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'refresh_token')
    # ### end Alembic commands ###
