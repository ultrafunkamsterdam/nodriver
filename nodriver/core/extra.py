import asyncio
import warnings

try:
    import bs4, lxml
except (ModuleNotFoundError, ImportError):
    print(
        """
            additional packages are required for this to work.
            to install these packages, run:
            
            pip install bs4 lxml
            """
    )


from . import element
from typing import Union, Text, ByteString


class HTMLDocument(bs4.BeautifulSoup):

    @classmethod
    async def create(cls, element_obj: element.Element):
        html = await element_obj.get_html()
        return cls(html, "lxml", element_obj.tab)
        # soup = await asyncio.get_running_loop().run_in_executor(
        #     bs4.BeautifulSoup, html, 'lxml'
        # )
        # instance = cls(soup)

    def __init__(self, html, features="lxml", tab=None):
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            raise Exception(
                (
                    "\n\n"
                    "the correct way of construction a '%(name)s' object is by using `await %(name)s.create(...)`"
                    "\n\n"
                )
                % dict(name=self.__class__.__name__)
            )
        super().__init__(html, features)
        self._tab = tab
