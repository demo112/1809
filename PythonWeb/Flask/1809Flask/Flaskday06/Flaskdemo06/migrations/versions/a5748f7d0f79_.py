"""empty message

Revision ID: a5748f7d0f79
Revises: 931aab686841
Create Date: 2018-12-28 11:14:03.710654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5748f7d0f79'
down_revision = '931aab686841'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('uage', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('uemail', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'uemail')
    op.drop_column('user', 'uage')
    # ### end Alembic commands ###
