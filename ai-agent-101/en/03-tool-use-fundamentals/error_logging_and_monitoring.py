"""Generated from book-content article."""

import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def execute_tool_with_logging(
    tool_name: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Execute tool with error logging."""
    
    start_time = datetime.now()
    
    try:
        result = execute_tool(tool_name, params)
        
        # Success log
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f"Tool '{tool_name}' succeeded in {duration}s")
        
        return {"success": True, "data": result}
    
    except Exception as e:
        # Failure log with details
        duration = (datetime.now() - start_time).total_seconds()
        logger.error(
            f"Tool '{tool_name}' failed in {duration}s",
            extra={
                "tool": tool_name,
                "params": params,
                "error_type": type(e).__name__,
                "error_message": str(e)
            }
        )
        
        return {"success": False, "error": str(e)}
