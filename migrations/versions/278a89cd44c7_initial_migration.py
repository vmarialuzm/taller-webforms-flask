"""initial migration

Revision ID: 278a89cd44c7
Revises: 
Create Date: 2023-04-11 18:01:13.872637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '278a89cd44c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Name', sa.String(length=25), nullable=True),
    sa.Column('CountryCode', sa.String(length=3), nullable=True),
    sa.Column('District', sa.String(length=20), nullable=True),
    sa.Column('Population', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city')
    # ### end Alembic commands ###
