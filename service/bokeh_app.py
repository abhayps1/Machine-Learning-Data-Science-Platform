from bokeh.server.server import Server
from tornado.web import RequestHandler

# Define your Bokeh application
def histogram_doc(doc):
    from bokeh.plotting import figure
    from bokeh.models import ColumnDataSource
    import numpy as np

    # Create some sample data
    data = np.random.randn(1000)
    hist, edges = np.histogram(data, bins=30)
    
    # Create a ColumnDataSource
    source = ColumnDataSource(data=dict(top=hist, left=edges[:-1], right=edges[1:]))
    
    # Create a figure
    p = figure(title="Histogram", tools="", background_fill_color="#fafafa")
    
    # Add a quad glyph
    p.quad(top='top', bottom=0, left='left', right='right', fill_color="navy", line_color="white", alpha=0.5, source=source)
    
    # Add the plot to the current document
    doc.add_root(p)

# Define a custom Tornado RequestHandler (optional)
class ChartHandler(RequestHandler):
    def get(self):
        self.write("This is a custom handler response")

# Get port from environment variable or use default
port = 5004

# Configuration values
server_name = "localhost"
charts_server_port = 5004

# Create and start the Bokeh server
server = Server(
    {'/histogram': histogram_doc},
    extra_patterns=[('/', ChartHandler)],
    allow_websocket_origin=[f"{server_name}:{charts_server_port}"],
    port=port
)

# Start the server and keep it running until interrupted
server.run_until_shutdown()
