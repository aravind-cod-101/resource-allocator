"""add table constraints

Revision ID: ed6e4c5e743f
Revises: 3c6f2a5a18c1
Create Date: 2026-02-07 23:24:09.937293

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "ed6e4c5e743f"
down_revision: Union[str, Sequence[str], None] = "3c6f2a5a18c1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_unique_constraint("uq_skills_name", "skills", ["name"])
    op.create_check_constraint(
        "ck_tasks_valid_date_range", "tasks", "start_date <= end_date"
    )
    op.create_check_constraint(
        "ck_resource_availability_valid_range",
        "resource_availability",
        "available_from <= available_to",
    )


def downgrade():
    op.drop_constraint(
        "ck_resource_availability_valid_range", "resource_availability", type_="check"
    )
    op.drop_constraint("ck_tasks_valid_date_range", "tasks", type_="check")
    op.drop_constraint("uq_skills_name", "skills", type_="unique")
