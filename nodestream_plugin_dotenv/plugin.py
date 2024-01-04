import os

from dotenv import load_dotenv
from nodestream.project import Project, ProjectPlugin


class DotEnvProjectPlugin(ProjectPlugin):
    def before_project_load(self, _: Project):
        load_dotenv(os.environ.get("NODESTREAM_DOTENV_PATH", ".env"))
