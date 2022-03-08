"""create_user_and_poll_tables

Revision ID: 6dd314e405bc
Revises: 
Create Date: 2022-03-08 22:43:09.992020

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6dd314e405bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(30), nullable=False, name='Username'),
        sa.Column('email', sa.String(100), nullable=False, name='Эл.почта'),
        sa.Column(),
    )


def downgrade():
    op.drop_table('users')