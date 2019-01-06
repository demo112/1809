"""empty message

Revision ID: 601a1ac07ca1
Revises: 80b427872774
Create Date: 2019-01-05 13:17:43.756185

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '601a1ac07ca1'
down_revision = '80b427872774'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('uemail', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('uphone', sa.String(length=11), nullable=True))
    op.drop_column('user', 'uname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('uname', mysql.VARCHAR(length=100), nullable=True))
    op.drop_column('user', 'uphone')
    op.drop_column('user', 'uemail')
    # ### end Alembic commands ###
