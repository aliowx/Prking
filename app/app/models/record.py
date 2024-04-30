from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    DateTime,
    Float,
)
from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.base_class import Base


class Record(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    ocr: Mapped[str] = mapped_column(String, index=True)

    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now, index=True
    )
    end_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now, index=True
    )

    score: Mapped[float] = mapped_column(
        Float, nullable=True, default=None, index=True
    )

    best_lpr_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("image.id", onupdate="CASCADE", ondelete="SET NULL"),
        index=True,
    )
    best_lpr = relationship("Image", foreign_keys=best_lpr_id)

    best_big_image_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("image.id", onupdate="CASCADE", ondelete="SET NULL"),
        index=True,
    )
    best_big_image = relationship("Image", foreign_keys=best_big_image_id)

    plates = relationship("Plate", back_populates="record")