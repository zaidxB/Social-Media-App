"""add content column to posts table

Revision ID: 910c5d855c7e
Revises: 56146da66c49
Create Date: 2026-07-22 19:49:23.903133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '910c5d855c7e'
down_revision: Union[str, Sequence[str], None] = '56146da66c49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
