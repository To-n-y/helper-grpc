"""'add_base_model'

Revision ID: 923ecae59a25
Revises: 60ffc5bbd577
Create Date: 2023-09-23 21:49:54.890952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '923ecae59a25'
down_revision: Union[str, None] = '60ffc5bbd577'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Comment', sa.Column('created_at', sa.TIMESTAMP(), nullable=False))
    op.create_unique_constraint(None, 'Comment', ['id'])
    op.add_column('Event', sa.Column('created_at', sa.TIMESTAMP(), nullable=False))
    op.create_unique_constraint(None, 'Event', ['id'])
    op.add_column('User', sa.Column('created_at', sa.TIMESTAMP(), nullable=False))
    op.create_unique_constraint(None, 'User', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'User', type_='unique')
    op.drop_column('User', 'created_at')
    op.drop_constraint(None, 'Event', type_='unique')
    op.drop_column('Event', 'created_at')
    op.drop_constraint(None, 'Comment', type_='unique')
    op.drop_column('Comment', 'created_at')
    # ### end Alembic commands ###