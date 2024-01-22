"""UniqueEmailConstraint

Revision ID: 64489ee8d227
Revises: b7626279bf60
Create Date: 2024-01-20 11:52:01.759643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64489ee8d227'
down_revision = 'b7626279bf60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['task_id'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['user_id'])
        batch_op.create_unique_constraint(None, ['user_email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
