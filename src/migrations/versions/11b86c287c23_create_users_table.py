"""create users table

Revision ID: 11b86c287c23
Revises: 
Create Date: 2023-05-26 14:05:08.203249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11b86c287c23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create the users table
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email')
    )


def downgrade() -> None:
    # Drop the users table
    op.drop_table('users')
