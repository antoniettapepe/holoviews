import json
import param

from ..widgets import NdWidget, SelectionWidget, ScrubberWidget

class BokehWidget(NdWidget):

    template = param.String(default='./bokehwidget.jinja')

    def __init__(self, plot, renderer=None, **params):
        super(BokehWidget, self).__init__(plot, renderer, **params)
        self.initialized = False

    def encode_frames(self, frames):
        frames = json.dumps(frames).replace('</', r'<\/')
        return frames

    def _plot_figure(self, idx):
        self.plot.update(idx, not self.initialized)
        figure_format = 'html' if self.embed or not self.initialized else 'json'
        self.initialized = True
        return self.renderer.html(self.plot, figure_format)



class SelectionWidget(BokehWidget, SelectionWidget):
    pass

class ScrubberWidget(BokehWidget, ScrubberWidget):
    pass
