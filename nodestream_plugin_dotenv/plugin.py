import os

from dotenv import load_dotenv
from nodestream.project import Project, ProjectPlugin


class DotEnvProjectPlugin(ProjectPlugin):
    def activate(self, _: Project):
        load_dotenv(os.environ.get("NODESTREAM_DOTENV_PATH", ".env"))
