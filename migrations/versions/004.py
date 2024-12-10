"""empty message

Revision ID: 004
Revises: 003
Create Date: 2024-12-10 11:47:52.596417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '004'
down_revision = '003'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deposition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('doi', sa.String(length=250), nullable=True),
    sa.Column('dep_metadata', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('doi')
    )
    op.create_table('community',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_community',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('community_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['community_id'], ['community.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'community_id')
    )
    with op.batch_alter_table('data_set', schema=None) as batch_op:
        batch_op.add_column(sa.Column('community_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'community', ['community_id'], ['id'])

    with op.batch_alter_table('feature_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uvl_valid', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feature_model', schema=None) as batch_op:
        batch_op.drop_column('uvl_valid')

    with op.batch_alter_table('data_set', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('community_id')

    op.drop_table('user_community')
    op.drop_table('community')
    op.drop_table('deposition')
    # ### end Alembic commands ###
