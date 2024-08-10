"""empty message

Revision ID: 576caa06ac38
Revises: 74c43a62d4db
Create Date: 2024-08-10 17:56:03.401676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '576caa06ac38'
down_revision = '74c43a62d4db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 't_post', ['post_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_article', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('post_id')

    # ### end Alembic commands ###
