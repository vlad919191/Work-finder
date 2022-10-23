"""fdsgfd

Revision ID: f5df2decbbae
Revises: f3f0cb73f2cf
Create Date: 2022-10-05 14:07:24.314143

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f5df2decbbae'
down_revision = 'f3f0cb73f2cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('work_experience', 'link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('work_experience', sa.Column('link', mysql.VARCHAR(length=220), nullable=True))
    # ### end Alembic commands ###