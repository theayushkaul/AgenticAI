from mcp.server import FastMCP

mcp = FastMCP("Math") # Server Name

@mcp.tool
def getWeather(location:str)->str:
    """Get the weather location."""
    return f"It is always raining in {location}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http") # Transport='streamable-http' argument tells the server to act as an http server to receive and respond to tool function calls