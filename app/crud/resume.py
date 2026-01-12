from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.resume import ResumeModel

async def get_latest_resume(db: AsyncSession):
    """
    Fetch the latest resume entry (ID desc)
    """
    result = await db.execute(select(ResumeModel).order_by(ResumeModel.id.desc()).limit(1))
    return result.scalars().first()
