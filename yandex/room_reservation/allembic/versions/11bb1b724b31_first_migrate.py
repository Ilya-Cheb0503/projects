"""first migrate

Revision ID: 11bb1b724b31
Revises: 
Create Date: 2024-01-19 07:34:38.428741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11bb1b724b31'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meetingroom',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meetingroom')
    # ### end Alembic commands ###