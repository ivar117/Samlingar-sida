"""posts table

Revision ID: 128e5e9a9689
Revises: 46ddd59875e4
Create Date: 2023-05-20 21:59:01.709132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '128e5e9a9689'
down_revision = '46ddd59875e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=31),
               type_=sa.String(length=32),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.String(length=32),
               type_=sa.VARCHAR(length=31),
               existing_nullable=True)

    # ### end Alembic commands ###
