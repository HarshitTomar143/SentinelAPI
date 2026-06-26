import uuid
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.finding import Finding

class Scan(Base):
    __tablename__ = "scans"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    base_url: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="queued",
    )

    progress: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    current_stage: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    health_score: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    started_at : Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    completed_at : Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at : Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    findings: Mapped[list["Finding"]]= relationship(
        back_populates= "scan",
        cascade="all , delete-orphan"
    )

# backpopulates means that suppose we scan has a relationship with findings and findings is also in a relationship with scan so that will tell the orm that these two relationships are same     
# cascade means that if we delete a scan then should the findings of the particlulare scan be exist, no? so using cascade we can delete that too