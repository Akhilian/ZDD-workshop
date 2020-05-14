"""add_identifier_to_flight

Revision ID: 4eec6bf6f749
Revises: c80d1c85bc3b
Create Date: 2020-05-14 09:52:43.872717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4eec6bf6f749'
down_revision = '7db359aedc20'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('flights', sa.Column('identifier', sa.String, nullable=False))


def downgrade():
    op.drop_column('flights', 'identifier')
