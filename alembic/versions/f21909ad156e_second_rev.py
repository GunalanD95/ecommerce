"""second rev

Revision ID: f21909ad156e
Revises: e64739327ff6
Create Date: 2021-10-12 07:00:39.850775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f21909ad156e'
down_revision = 'e64739327ff6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "shop",
        sa.Column('available_products',sa.Integer)
    )


def downgrade():
    op.drop_column(
        "shop",
        "available_products"
    )