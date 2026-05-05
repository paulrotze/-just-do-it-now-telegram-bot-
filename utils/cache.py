"""
Модуль кэширования для оптимизации производительности.
"""
import asyncio
from datetime import datetime, timedelta
from typing import Optional, List, Dict


class LeaderboardCache:
    """Кэш для лидерборда с автообновлением"""
    
    def __init__(self, ttl_seconds: int = 300):
        self.ttl = timedelta(seconds=ttl_seconds)
        self._cache: Optional[List[Dict]] = None
        self._expires_at: Optional[datetime] = None
        self._lock = asyncio.Lock()
    
    async def get(self, db) -> List[Dict]:
        """Получить данные из кэша или обновить их"""
        async with self._lock:
            if self._is_valid():
                return self._cache or []
            
            self._cache = await db.get_top_users_by_streak(10)
            self._expires_at = datetime.now() + self.ttl
            return self._cache
    
    def _is_valid(self) -> bool:
        """Проверить актуальность кэша"""
        return (
            self._cache is not None and 
            self._expires_at is not None and 
            datetime.now() < self._expires_at
        )
    
    def invalidate(self):
        """Сбросить кэш"""
        self._cache = None
        self._expires_at = None


# Глобальный экземпляр кэша с TTL 5 минут
leaderboard_cache = LeaderboardCache(ttl_seconds=300)
