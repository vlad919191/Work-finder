"""efs

Revision ID: 42d128e50475
Revises: 84e325b0c1ee
Create Date: 2022-10-15 00:34:16.347156

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '42d128e50475'
down_revision = '84e325b0c1ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('skill', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'skill', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'skill', type_='foreignkey')
    op.alter_column('skill', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###