"""update products

Revision ID: 31abc09eb2a7
Revises:
Create Date: 2022-08-01 20:26:05.580807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31abc09eb2a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('brand', sa.String(200), nullable=False),
        sa.Column('name', sa.String(200)),
        sa.Column('price', sa.Integer),
    )


def downgrade():
    op.drop_table('product')
