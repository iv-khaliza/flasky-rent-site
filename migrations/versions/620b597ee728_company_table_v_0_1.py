"""company_table_v.0.1

Revision ID: 620b597ee728
Revises: 
Create Date: 2024-05-23 02:30:52.812841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '620b597ee728'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('body', sa.String(length=512), nullable=False),
    sa.Column('phone', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_company_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_company_name'), ['name'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_company_name'))
        batch_op.drop_index(batch_op.f('ix_company_email'))

    op.drop_table('company')
    # ### end Alembic commands ###
