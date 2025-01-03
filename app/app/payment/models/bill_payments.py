from sqlalchemy import JSON, ForeignKey, Integer, String, BigInteger, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base


class Transaction(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    transaction_number: Mapped[str] = mapped_column(
        String, nullable=True, index=True
    )

    bill_ids: Mapped[list[int]] = mapped_column(ARRAY(Integer), nullable=True)

    status: Mapped[str] = mapped_column(String, nullable=True)

    order_id_paymet_switch: Mapped[int | None] = mapped_column(
        BigInteger, nullable=True, unique=True
    )

    order_id_b2b: Mapped[int | None] = mapped_column(
        BigInteger, nullable=True, unique=True
    )

    amount: Mapped[int] = mapped_column(BigInteger, nullable=True)

    callback_url: Mapped[str | None] = mapped_column(String, nullable=True)

    user_id: Mapped[int] = mapped_column(Integer, nullable=True)

    rrn: Mapped[str] = mapped_column(String, nullable=True)
