"""fgd

Revision ID: 20a4c424baa3
Revises: 
Create Date: 2022-10-02 17:21:43.551882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20a4c424baa3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('access_token', sa.String(length=320), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('password_hash', sa.String(length=200), nullable=False),
    sa.Column('first_name', sa.String(length=60), nullable=False),
    sa.Column('last_name', sa.String(length=60), nullable=False),
    sa.Column('date_birth', sa.Date(), nullable=False),
    sa.Column('email_address', sa.String(length=120), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('image_path', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('auth')
    # ### end Alembic commands ###