from mcp.server.fastmcp import FastMCP

mcp = FastMCP("EntryPoint Demo Server")


@mcp.tool()
def calculate_streak_bonus(days: int) -> int:
    """מחשב בונוס נקודות לפי מספר ימי רצף (streak) של מלווה."""
    if days >= 30:
        return days * 3
    if days >= 7:
        return days * 2
    return days


@mcp.tool()
def get_role_categories(role: str) -> list[str]:
    """מחזיר את קטגוריות הלמידה המומלצות עבור תפקיד יעד."""
    catalog = {
        "devops": ["Linux", "Docker", "Kubernetes", "CI/CD", "Cloud"],
        "backend": ["Databases", "API Design", "Auth", "Testing", "System Design"],
    }
    return catalog.get(role.lower(), ["role not found"])


if __name__ == "__main__":
    mcp.run()
