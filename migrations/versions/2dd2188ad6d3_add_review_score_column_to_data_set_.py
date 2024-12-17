"""Add review_score column to data_set table

Revision ID: 2dd2188ad6d3
Revises: 004
Create Date: 2024-12-14 20:43:17.853325

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2dd2188ad6d3'
down_revision = '004'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fake_nodo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('doi', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dataset_review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('data_set_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('value >= 1 AND value <= 5', name='check_value_range_dataset'),
    sa.ForeignKeyConstraint(['data_set_id'], ['data_set.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feature_model_review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('feature_model_id', sa.Integer(), nullable=True),
    sa.CheckConstraint('value >= 1 AND value <= 5', name='check_value_range_model'),
    sa.ForeignKeyConstraint(['feature_model_id'], ['feature_model.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('deposition', schema=None) as batch_op:
        batch_op.drop_index('doi')

    op.drop_table('deposition')
    with op.batch_alter_table('data_set', schema=None) as batch_op:
        batch_op.add_column(sa.Column('review_score', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_set', schema=None) as batch_op:
        batch_op.drop_column('review_score')

    op.create_table('deposition',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('status', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('doi', mysql.VARCHAR(length=250), nullable=True),
    sa.Column('dep_metadata', mysql.LONGTEXT(charset='utf8mb4', collation='utf8mb4_bin'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('deposition', schema=None) as batch_op:
        batch_op.create_index('doi', ['doi'], unique=True)

    op.drop_table('feature_model_review')
    op.drop_table('dataset_review')
    op.drop_table('fake_nodo')
    # ### end Alembic commands ###
