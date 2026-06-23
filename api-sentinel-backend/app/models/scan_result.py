import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class ScanResult(Base):
    __tablename__ = "scan_results"

    id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,    
        )
    
    scan_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("scans.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    success_rate : Mapped[float] = mapped_column(
        Float, 
        default= 0,
    )

    avg_latency: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    min_latency: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    max_latency: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    p95_latency: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    https_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    rate_limiting_detected: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    health_score: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
