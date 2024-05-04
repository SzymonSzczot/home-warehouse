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


def upgrade():
    # Create items_catalog_category table
    op.create_table(
        'items_catalog_category',
        sa.Column('id', sa.UUID, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('description', sa.String),
    )

    # Create items_catalog table
    op.create_table(
        'items_catalog',
        sa.Column('id', sa.UUID, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('image_url', sa.String),
        sa.Column('description', sa.String),
        sa.Column('category_id', sa.UUID, sa.ForeignKey('items_catalog_category.id')),
    )


def downgrade():
    # Drop items_catalog table
    op.drop_table('items_catalog')

    # Drop items_catalog_category table
    op.drop_table('items_catalog_category')
