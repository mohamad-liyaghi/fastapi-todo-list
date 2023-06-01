"""uuid task

Revision ID: 8999b73b0f95
Revises: 3f1925045908
Create Date: 2023-05-31 15:16:08.326395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8999b73b0f95'
down_revision = '3f1925045908'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('uuid', sa.UUID(), nullable=False))
    op.create_unique_constraint(None, 'tasks', ['uuid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='unique')
    op.drop_column('tasks', 'uuid')
    # ### end Alembic commands ###