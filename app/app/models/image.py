from sqlalchemy import Integer, ForeignKey, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import LargeBinary

from app.db.base_class import Base


class Image(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    image: Mapped[str] = mapped_column(LargeBinary, nullable=True)

    path_image: Mapped[str] = mapped_column(String, nullable=True)

    camera_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("equipment.id", ondelete="SET NULL", onupdate="CASCADE"),
        nullable=True,
        index=True,
    )
    camera_rel = relationship("Equipment", foreign_keys=camera_id)

    additional_data: Mapped[dict] = mapped_column(JSON, nullable=True)
