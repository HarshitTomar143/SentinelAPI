import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.scan import Scan

class Finding(Base):
    __tablename__ = "findings"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default= uuid.uuid4,
    )

    scan_id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("scans.id", ondelete="CASCADE"),
        nullable=False,
    )

    severity : Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    title : Mapped[str] = mapped_column(
        String,
        nullable=False, 
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable= False,
    )

    recommendation: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    scan : Mapped["Scan"] = relationship(
        back_populates="findings"
    )