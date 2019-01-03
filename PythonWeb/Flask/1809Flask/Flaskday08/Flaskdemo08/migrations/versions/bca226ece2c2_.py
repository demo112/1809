"""empty message

Revision ID: bca226ece2c2
Revises: 2a4d08ce67fa
Create Date: 2019-01-03 11:00:30.613016

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bca226ece2c2'
down_revision = '2a4d08ce67fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher')
    op.drop_table('student')
    op.drop_table('teacher_student')
    op.drop_table('user')
    op.drop_index('teacher_id', table_name='wife')
    op.drop_index('user_id', table_name='wife')
    op.drop_table('wife')
    op.drop_table('course')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('cname', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('wife',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('wname', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('wage', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('teacher_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], name='wife_ibfk_2'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='wife_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('user_id', 'wife', ['user_id'], unique=True)
    op.create_index('teacher_id', 'wife', ['teacher_id'], unique=True)
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('uname', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('uage', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('uemail', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('isActive', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('teacher_student',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('teacher_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('student_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], name='teacher_student_ibfk_2'),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], name='teacher_student_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('student',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('sname', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('sage', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('isActive', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('teacher',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('tname', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('tage', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('course_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name='teacher_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
