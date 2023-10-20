"""empty message

Revision ID: e313d12b2b51
Revises: 
Create Date: 2023-10-20 13:08:53.808085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e313d12b2b51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password_digest', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('order_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('closed', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users_table.id'], name=op.f('fk_order_table_user_id_users_table')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orderproduct_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order_table.id'], name=op.f('fk_orderproduct_table_order_id_order_table')),
    sa.ForeignKeyConstraint(['product_id'], ['product_table.id'], name=op.f('fk_orderproduct_table_product_id_product_table')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orderproduct_table')
    op.drop_table('order_table')
    op.drop_table('users_table')
    op.drop_table('product_table')
    # ### end Alembic commands ###