"""create-plane-table

Revision ID: 7425d9bb905a
Revises: 
Create Date: 2020-04-23 18:45:54.328544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7425d9bb905a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'planes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('places', sa.Integer, nullable=True),
    )

def downgrade():
    op.drop_table('planes')
