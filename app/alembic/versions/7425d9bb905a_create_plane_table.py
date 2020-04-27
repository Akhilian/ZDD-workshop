"""create-plane-table

Revision ID: 7425d9bb905a
Revises:
Create Date: 2020-04-23 18:45:54.328544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

revision = '7425d9bb905a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'identifier',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('code', sa.String(7), nullable=False),
    )

    op.create_table(
        'planes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('places', sa.Integer, nullable=True),
        sa.Column('planeIdentifierId', sa.Integer, ForeignKey('identifier.id'), nullable=False),
    )

def downgrade():
    op.drop_table('planes')
    op.drop_table('identifier')
