"""create_flight_table

Revision ID: 7db359aedc20
Revises: 7425d9bb905a
Create Date: 2020-05-02 20:36:53.472266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

revision = '7db359aedc20'
down_revision = '7425d9bb905a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'flights',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('start_time', sa.DateTime, nullable=True),
        sa.Column('duration', sa.Integer, nullable=True),
        sa.Column('status', sa.String, nullable=False),
        sa.Column('planeId', sa.Integer, ForeignKey('planes.id'))
    )


def downgrade():
    op.drop_table('flights')
