"""the first rev

Revision ID: e64739327ff6
Revises: 
Create Date: 2021-10-12 06:41:15.402478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e64739327ff6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "shop",
        sa.Column("id",sa.Integer,primary_key=True,index=True),
        sa.Column("title",sa.String),
        sa.Column("description",sa.Text),
        sa.Column("price",sa.Integer)
    )

def downgrade():
    op.drop_table("shop")
