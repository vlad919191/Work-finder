"""vacancy

Revision ID: 3cb0de38aa04
Revises: a78d9530b4d8
Create Date: 2022-10-13 14:52:29.251775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cb0de38aa04'
down_revision = 'a78d9530b4d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vacancy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('short_description', sa.String(length=600), nullable=False),
    sa.Column('long_description', sa.Text(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.Column('rubric_id', sa.Integer(), nullable=False),
    sa.Column('creation_date', sa.Date(), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacancy')
    # ### end Alembic commands ###