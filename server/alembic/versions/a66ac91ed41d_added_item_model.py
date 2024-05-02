"""Added Item model

Revision ID: a66ac91ed41d
Revises: 
Create Date: 2024-05-01 12:26:18.179811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a66ac91ed41d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'items_catalog',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String),
    )


def downgrade():
    op.drop_table('items_catalog')
