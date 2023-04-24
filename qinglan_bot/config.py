from typing import Optional
from mcqq_tool.config import Config as BaseModel


class Config(BaseModel):
    """配置"""
    # 是否开启 @Bot
    mc_qq_to_me: Optional[bool] = True
    # 数据库路径
    mc_qq_dir: Optional[str] = ""
