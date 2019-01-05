"""empty message

Revision ID: 40de0ef2d884
Revises: 
Create Date: 2019-01-04 09:29:03.765393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40de0ef2d884'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uname', sa.String(length=30), nullable=True),
    sa.Column('upwd', sa.String(length=200), nullable=True),
    sa.Column('nickname', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
