"""empty message

Revision ID: e05a6272d019
Revises: 9ddb1fc5e27e
Create Date: 2024-03-25 10:07:05.339956

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e05a6272d019'
down_revision = '9ddb1fc5e27e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('complaints', schema=None) as batch_op:
        batch_op.add_column(sa.Column('send_details', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('received_details', sa.String(length=255), nullable=True))
        batch_op.drop_column('details')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('complaints', schema=None) as batch_op:
        batch_op.add_column(sa.Column('details', mysql.VARCHAR(length=255), nullable=False))
        batch_op.drop_column('received_details')
        batch_op.drop_column('send_details')

    # ### end Alembic commands ###
