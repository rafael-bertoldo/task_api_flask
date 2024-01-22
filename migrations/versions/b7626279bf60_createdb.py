"""CreateDb

Revision ID: b7626279bf60
Revises: 
Create Date: 2024-01-20 11:31:09.549796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7626279bf60'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.String(length=36), nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('user_email', sa.String(), nullable=False),
    sa.Column('user_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('tasks',
    sa.Column('task_id', sa.String(length=36), nullable=False),
    sa.Column('task_content', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('task_id'),
    sa.UniqueConstraint('task_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    op.drop_table('users')
    # ### end Alembic commands ###