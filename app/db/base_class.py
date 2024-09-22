from typing import Any, Optional, Dict

from sqlalchemy.ext.declarative import as_declarative, declared_attr

class_registry: Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    """
    This is similar to:    Base = declarative_base()
    We are using this to generate a table name automatically
    """
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
