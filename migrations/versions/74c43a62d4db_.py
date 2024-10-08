"""empty message

Revision ID: 74c43a62d4db
Revises: c04239b75198
Create Date: 2024-07-14 14:51:14.535132

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '74c43a62d4db'
down_revision = 'c04239b75198'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_photo', schema=None) as batch_op:
        batch_op.alter_column('photo',
               existing_type=postgresql.BYTEA(),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_photo', schema=None) as batch_op:
        batch_op.alter_column('photo',
               existing_type=sa.Text(),
               type_=postgresql.BYTEA(),
               existing_nullable=True)

    # ### end Alembic commands ###
