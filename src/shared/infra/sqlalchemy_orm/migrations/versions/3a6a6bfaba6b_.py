"""empty message

Revision ID: 3a6a6bfaba6b
Revises: 5392a03e9f53
Create Date: 2024-02-13 04:00:31.533315

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "3a6a6bfaba6b"
down_revision: Union[str, None] = "5392a03e9f53"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "publisher",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("city", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column(
        "post", sa.Column("publisher_id", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        None, "post", "publisher", ["publisher_id"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "post", type_="foreignkey")
    op.drop_column("post", "publisher_id")
    op.drop_table("publisher")
    # ### end Alembic commands ###
