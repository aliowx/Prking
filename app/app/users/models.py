from sqlalchemy import Boolean, Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base_class import Base

from app.acl.role import UserRoles


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(50), nullable=True)
    username: Mapped[str] = mapped_column(
        String(50), index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    is_active: Mapped[bool] = mapped_column(
        Boolean(), default=True, nullable=True
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean(), default=False, nullable=True
    )

    """
    def upgrade() -> None:
        # ### commands auto generated by Alembic - please adjust! ###
        op.execute("DROP TYPE userroles CASCADE;")
        op.execute(
            "CREATE TYPE userroles AS ENUM ('ADMINISTRATOR', 'PARKING_MANAGER', 'TECHNICAL_SUPPORT', 'OPERATIONAL_STAFF', 'REPORTING_ANALYSIS', 'SECURITY_STAFF', 'EXIT_GATE_DOOR');"
        )
        op.add_column(
            "user",
            sa.Column(
                "role",
                sa.Enum(
                    "ADMINISTRATOR",
                    "PARKING_MANAGER",
                    "TECHNICAL_SUPPORT",
                    "OPERATIONAL_STAFF",
                    "REPORTING_ANALYSIS",
                    "SECURITY_STAFF",
                    "EXIT_GATE_DOOR",
                    name="userroles",
                ),
                nullable=True,
            ),
        )
        op.alter_column(
            "user", "is_active", existing_type=sa.BOOLEAN(), nullable=True
        )
        op.alter_column(
            "user", "is_superuser", existing_type=sa.BOOLEAN(), nullable=True
        )
    # ### end Alembic commands ###


    def downgrade() -> None:
        # ### commands auto generated by Alembic - please adjust! ###
        op.alter_column(
            "user", "is_superuser", existing_type=sa.BOOLEAN(), nullable=False
        )
        op.alter_column(
            "user", "is_active", existing_type=sa.BOOLEAN(), nullable=False
        )
        op.drop_column("user", "role")
        op.execute("DROP TYPE userroles;")
    """
    role = mapped_column(
        Enum(UserRoles, name="userroles", create_type=True),
        nullable=True,
    )
