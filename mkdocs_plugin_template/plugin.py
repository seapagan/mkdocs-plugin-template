"""Main Class for this Plugin."""
import re
from typing import Literal

from mkdocs.plugins import BasePlugin


class TemplatePlugin(BasePlugin):
    """Class for the 'mkdocs-plugin-template'."""

    def __init__(self):
        """Set up variables for this plugin.

        Any variables required throughout the class, set them here
        eg:
        self.my_var = None
        """
        self.plugin_tag = "plugin-template"

    def on_startup(
        self, command: Literal["build", "gh-deploy", "serve"], **kwargs
    ):
        """Use new mkdocs 1.4 plugin system.

        The presence of an on_startup method (even if empty) migrates the plugin
        to the new system where the plugin object is kept across builds within
        one mkdocs serve.

        Here you can do any processing that needs to be done when the build
        first starts, but only once per mkdocs build/serve.
        """

    def on_page_markdown(self, markdown: str, **kwargs) -> str | None:
        """Modify the markdown if our tag is present.

        This is called for every markdown file, so we need to check if our tag
        is here before doing anything. If not, jsut return the markdown as is.
        """
        cmds = re.finditer(
            pattern=(rf"{{{{\s*{self.plugin_tag}\s*}}}}"),
            string=markdown,
            flags=re.IGNORECASE,
        )
        if cmds:
            for match in cmds:
                # We have one or more match, so we need to do whatever we want
                # to do for this plugin here.

                output = "This is the output of our plugin."
                # replace the tag with the output of the command
                markdown = markdown.replace(match.group(0), output, 1)

        return markdown
