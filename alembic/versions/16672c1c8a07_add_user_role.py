"""add user_role

Revision ID: 16672c1c8a07
Revises: 93fccc07673b
Create Date: 2023-09-25 22:58:18.863916

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16672c1c8a07'
down_revision: Union[str, None] = '93fccc07673b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('role', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'role')
    # ### end Alembic commands ###