"""Proposal.status

Revision ID: 3c47ba103724
Revises: 6f98e24760d
Create Date: 2014-01-28 00:09:39.231864

"""

# revision identifiers, used by Alembic.
revision = '3c47ba103724'
down_revision = '6f98e24760d'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from funnel.models import PROPOSALSTATUS


def upgrade():
    connection = op.get_bind()
    proposal = table('proposal',
        column(u'confirmed', sa.BOOLEAN()),
        column(u'status', sa.Integer))
    connection.execute(proposal.update().where(proposal.c.confirmed == True).values({proposal.c.status: PROPOSALSTATUS.CONFIRMED}))
    connection.execute(proposal.update().where(proposal.c.confirmed == False).values({proposal.c.status: PROPOSALSTATUS.SUBMITTED}))
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('proposal', u'confirmed')
    ### end Alembic commands ###


def downgrade():
    connection = op.get_bind()
    proposal = table('proposal',
        column(u'confirmed', sa.BOOLEAN()),
        column(u'status', sa.Integer))
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proposal', sa.Column(u'confirmed', sa.BOOLEAN(), server_default="False", nullable=False))
    ### end Alembic commands ###
    connection.execute(proposal.update().where(proposal.c.status == PROPOSALSTATUS.CONFIRMED).values({proposal.c.confirmed: True}))
    connection.execute(proposal.update().values({proposal.c.status: 0}))
    op.alter_column('proposal', u'confirmed', server_default=None)
