"""이제 닉네임을 추천할 수 있습니다 -bean12.

Revision ID: 1561a57ed187
Revises: 4d05aeb1e963
Create Date: 2016-02-19 13:38:10.971959

"""

# revision identifiers, used by Alembic.
revision = '1561a57ed187'
down_revision = '4d05aeb1e963'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nickrecom',
    sa.Column('idx', sa.Integer(), nullable=False),
    sa.Column('nick', sa.String(length=50), nullable=True),
    sa.Column('fromA', sa.String(length=50), nullable=True),
    sa.Column('toB', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('idx')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nickrecom')
    ### end Alembic commands ###
