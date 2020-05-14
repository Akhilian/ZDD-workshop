"""add_position_to_a_flight

Revision ID: c80d1c85bc3b
Revises: 7db359aedc20
Create Date: 2020-05-03 13:43:55.884523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

revision = 'c80d1c85bc3b'
down_revision = '4eec6bf6f749'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'positions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('latitude', sa.Float, nullable=True),
        sa.Column('longitude', sa.Float, nullable=True),
        sa.Column('flightId', sa.Integer, ForeignKey('flights.id'))
    )


def downgrade():
    op.drop_table('positions')
