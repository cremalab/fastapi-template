"""example

Revision ID: 5e16b03b6cf6
Revises: 
Create Date: 2024-08-09 20:21:44.969511

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5e16b03b6cf6"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # This function is auto created by alembic, and you need to write the executable script
    op.create_table(
        "example_table",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("description", sa.Text, nullable=True),
    )


def downgrade() -> None:
    # This function is also auto created, and you need to write the script to undo exactly what was written in upgrade,
    # this way, if an error occurs it can be handled appropriately
    op.drop_table("example_table")
