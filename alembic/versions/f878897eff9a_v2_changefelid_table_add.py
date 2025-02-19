"""v2_changefelid_table_add

Revision ID: f878897eff9a
Revises: 9b36c03a8636
Create Date: 2025-01-17 15:32:05.875477

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f878897eff9a'
down_revision: Union[str, None] = '9b36c03a8636'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=500),
               existing_nullable=True)
    op.alter_column('posts', 'caption',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=500),
               existing_nullable=True)
    op.alter_column('posts', 'image_url',
               existing_type=sa.VARCHAR(length=550),
               type_=sa.String(length=1000),
               existing_nullable=True)
    op.alter_column('user', 'first_name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=500),
               existing_nullable=True)
    op.alter_column('user', 'last_name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=500),
               existing_nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=500),
               existing_nullable=True)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=500),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('user', 'last_name',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('user', 'first_name',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('posts', 'image_url',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=550),
               existing_nullable=True)
    op.alter_column('posts', 'caption',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)
    op.alter_column('posts', 'title',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)
    # ### end Alembic commands ###
