from mcp.server.fastmcp import FastMCP
mcp=FastMCP("Weather")
@mcp.tool()

async def get_weather(location:str) -> str:
    """
    get weather loaction

    """
    return "It's raining in california"

if __name__ == "__main__":
    mcp.run(transport="streamble-http")
    