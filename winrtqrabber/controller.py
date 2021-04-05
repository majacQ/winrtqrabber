import logging
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from pyzbar.pyzbar import Decoded
    from winrtqrabber.view import ScannerView

_LOGGER = logging.getLogger(__name__)


class Controller:
    def __init__(self, model, view: "ScannerView"):
        self._model = model
        self.view = view

    async def start_scan(self):
        resolution = await self._model.prepare_webcam()
        self.view.set_preview_size(*resolution)
        await self._model.start(self.view.set_frame)

    async def stop_scan(self, result: Optional["Decoded"] = None):
        await self._model.stop()
        if result:
            print(result)
