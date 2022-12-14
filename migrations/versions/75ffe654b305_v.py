"""v

Revision ID: 75ffe654b305
Revises: f82c25444706
Create Date: 2022-10-13 22:37:23.539335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75ffe654b305'
down_revision = 'f82c25444706'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vacancy', 'creation_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vacancy', sa.Column('creation_date', sa.DATE(), nullable=True))
    # ### end Alembic commands ###
